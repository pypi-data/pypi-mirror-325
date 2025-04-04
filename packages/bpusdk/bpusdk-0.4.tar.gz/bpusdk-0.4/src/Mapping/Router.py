from pathlib import Path

import numpy as np
from loguru import logger

from BrainpyLib.Common import Fake, array_to_hex, div_round_up, save_hex_file

DIRECTION_NAME = ('WEST', 'SOUTH', 'EAST', 'NORTH')

FIVE_DIRECTION = range(5)


class DIRECTION:
    WEST = 0
    SOUTH = 1
    EAST = 2
    NORTH = 3
    LOCAL = 4


class OneChip:
    def __init__(self, chip_id) -> None:
        self.id = chip_id
        self.edge_count = 0
        self.vertex_count = 0
        self.vertex = []    # chip vertex
        self.edge_map = {}  # edges with the dst vertex in chip
        self.msg_queue = []
        self.msg_queue_next = [[] for _ in range(5)]
        self.neighbor_chips = {}  # {OneChip * 4}
        self.routing_table = {}  # Dict{routing: {src_v: <W, S, E, N, Local>}}
        self.bfs_record = {}


class Router():
    def __init__(self, config, neuron_num) -> None:
        self.X_NumOfChips = config['X_TileNum']
        self.Y_NumOfChips = config['Y_TileNum']

        # Router need the original layout
        self.NPUNumOfChip = config['Tile_NpuNum']
        self.NodeNumOfNpu = config['Npu_NeuronNum']
        self.RouterGroupRange = config['Router_GroupNum']
        self.GroupNumOfChip = self.NPUNumOfChip * \
            self.NodeNumOfNpu // self.RouterGroupRange
        self.neuron_num = neuron_num
        self.Is_Y_First = config['Is_Y_First']

        used_group = div_round_up(neuron_num, self.RouterGroupRange)
        used_chip = div_round_up(used_group, self.GroupNumOfChip)
        used_y = div_round_up(used_chip, self.X_NumOfChips)
        if used_y > self.Y_NumOfChips:
            logger.critical(
                f'Error: {neuron_num} neurons can not load into {self.NPUNumOfChip} chips.')
            exit(1)

        if not self.Is_Y_First:
            used_y = div_round_up(used_chip, self.X_NumOfChips)
            self.Y_NumOfChips = used_y
            if used_y == 1:
                self.X_NumOfChips = used_chip
        else:
            used_x = div_round_up(used_chip, self.Y_NumOfChips)
            self.X_NumOfChips = used_x
            if used_x == 1:
                self.Y_NumOfChips = used_chip

        # print(f'used_xy = {self.X_NumOfChips, self.Y_NumOfChips}')

        # init chip matrix
        self.TotalChips = self.X_NumOfChips * self.Y_NumOfChips
        self.chip_matrix = [OneChip(i) for i in range(self.TotalChips)]
        self.npu_num = self.GroupNumOfChip * self.TotalChips

        # npus into chips
        self.npus_to_chips = []
        for i in range(self.TotalChips):
            self.npus_to_chips.extend([i] * self.GroupNumOfChip)

        # build chip connection
        """ 需要区分芯片排列是X还是Y优先
        X优先: 0——>1 方向往东 e.g.[
        0 1 2
        3 4 5
        6 7 8]
        Y优先: 0——>1 方向往南 e.g.[
        0 3 6
        1 4 7
        2 5 8]
        """
        for i in range(self.TotalChips):
            if self.Is_Y_First:
                north = i - 1
                south = i + 1
                west = i - self.Y_NumOfChips
                east = i + self.Y_NumOfChips
            else:
                north = i - self.X_NumOfChips
                south = i + self.X_NumOfChips
                west = i - 1
                east = i + 1
            x, y = self.convert_id_to_xy(i)
            if y > 0:
                self.chip_matrix[i].neighbor_chips[DIRECTION.NORTH] = self.chip_matrix[north]
            if y < self.Y_NumOfChips-1:
                self.chip_matrix[i].neighbor_chips[DIRECTION.SOUTH] = self.chip_matrix[south]
            if x > 0:
                self.chip_matrix[i].neighbor_chips[DIRECTION.WEST] = self.chip_matrix[west]
            if x < self.X_NumOfChips - 1:
                self.chip_matrix[i].neighbor_chips[DIRECTION.EAST] = self.chip_matrix[east]

        # for i in range(self.TotalChips):
        #     for neighb in self.chip_matrix[i].neighbor_chips:
        #         print(self.chip_matrix[i].neighbor_chips[neighb].id)

        self.router_load = np.zeros(
            (self.TotalChips, 5), dtype=np.int64)

    def convert_id_to_xy(self, chip_id):
        if self.Is_Y_First:
            chip_x = chip_id // self.Y_NumOfChips
            chip_y = chip_id % self.Y_NumOfChips
        else:
            chip_x = chip_id % self.X_NumOfChips
            chip_y = chip_id // self.X_NumOfChips

        return chip_x, chip_y

    def get_one_src_routing(self, src_id, dst_id_list):
        """_summary_

        Parameters
        ----------
        src_id : int
            Routing source chip id
        dst_id_list : list [id_0, id_1, ...]
            Routing target chips id collaction

        """
        routing = np.zeros((self.TotalChips, 5))
        routing_record = [routing]
        path_lens = [-1] * self.TotalChips
        src_x, src_y = self.convert_id_to_xy(src_id)
        dst_set = []
        src_set = [src_id]
        path_lens[src_id] = 0

        # straight forward
        for dst_id in dst_id_list:
            dst_x, dst_y = self.convert_id_to_xy(dst_id)

            # get direction
            diff_x = src_x - dst_x
            diff_y = src_y - dst_y

            if diff_x != 0 and diff_y != 0:
                dst_set.append(dst_id)
                continue

            if diff_x < 0:
                direct = DIRECTION.EAST    # East
            elif diff_x > 0:
                direct = DIRECTION.WEST    # West
            elif diff_y < 0:
                direct = DIRECTION.SOUTH    # South
            elif diff_y > 0:
                direct = DIRECTION.NORTH    # North

            diff = abs(diff_x) + abs(diff_y)
            current_id = src_id
            current_dist = 0
            for i in range(diff):
                routing[current_id, direct] = 1
                current_id = self.chip_matrix[current_id].neighbor_chips[direct].id
                src_set.append(current_id)
                current_dist = current_dist + 1
                path_lens[current_id] = current_dist
            routing[current_id, DIRECTION.LOCAL] = 1
            routing_record.append(routing)

        # logger.info(
        #     f'Finish straight forward, routing_record: \n{np.array(routing)}')

        # non-straight forward
        src_set = list(set(src_set))
        loop_cnt = -1
        while len(dst_set) > 0:
            loop_cnt = loop_cnt + 1
            # logger.info(
            #     f'\n\n===================Non-Straight Forward: Loop {loop_cnt}===================')
            # logger.info(f'src_set: {src_set}')
            # logger.info(f'dst_set: {dst_set}')
            src_cands = []
            dst_cands = []
            dist_cands = []

            # l1_dist
            for dst_id in dst_set:
                dst_x, dst_y = self.convert_id_to_xy(dst_id)
                l1_dist = abs(src_x - dst_x) + abs(src_y - dst_y)

                dist = []
                for src in src_set:
                    x, y = self.convert_id_to_xy(src)
                    dist.append(abs(dst_x-x) + abs(dst_y-y))

                find_flag = False
                while not find_flag:
                    min_dist = min(dist)
                    src_cands_tmp = [s
                                     for i, s in enumerate(src_set) if dist[i] == min_dist]
                    dist_cands_tmp = np.array([
                        path_lens[i] for i in src_cands_tmp]) + min_dist
                    # check is l1_dist
                    bypass_filted_idx = []
                    for i, d in enumerate(dist_cands_tmp):
                        if d == l1_dist or 1:
                            bypass_filted_idx.append(i)
                    if len(bypass_filted_idx) > 0:
                        src_cands.extend([src_cands_tmp[i]
                                         for i in bypass_filted_idx])
                        dst_cands.extend(
                            len([src_cands_tmp[i] for i in bypass_filted_idx]) * [dst_id])
                        dist_cands.extend(
                            len([src_cands_tmp[i] for i in bypass_filted_idx]) * [min_dist])
                        find_flag = True

            # logger.info(f'src_cands = {src_cands}')
            # logger.info(f'dst_id = {dst_cands}')

            # choose min cands
            min_dist = min(dist_cands)
            min_src_dist = self.TotalChips
            for s, d, di in zip(src_cands, dst_cands, dist_cands):
                if di == min_dist and path_lens[s] < min_src_dist:
                    filted_src_cand = s
                    filted_dst_cand = d
                    min_src_dist = path_lens[s]

            # logger.info(
            #     f'Filted src_id = {filted_src_cand}, dst_id = {filted_dst_cand}')

            # search path
            src_cand_x, src_cand_y = self.convert_id_to_xy(filted_src_cand)
            dst_cand_x, dst_cand_y = self.convert_id_to_xy(filted_dst_cand)
            diff_x = src_cand_x - dst_cand_x
            diff_y = src_cand_y - dst_cand_y

            if diff_x <= 0:
                direct_x = DIRECTION.EAST    # East
            else:
                direct_x = DIRECTION.WEST    # West

            if diff_y <= 0:
                direct_y = DIRECTION.SOUTH    # South
            else:
                direct_y = DIRECTION.NORTH    # North

            diff_x = abs(diff_x)
            diff_y = abs(diff_y)

            # current location
            current_id = filted_src_cand
            current_dist = path_lens[current_id]

            while diff_x > 0 or diff_y > 0:
                if (self.router_load[current_id, direct_x] > self.router_load[current_id, direct_y] or diff_x <= 0) and diff_y > 0:
                    diff_y = diff_y - 1
                    routing[current_id, direct_y] = 1
                    current_id = self.chip_matrix[current_id].neighbor_chips[direct_y].id
                    src_set.append(current_id)

                    current_dist = current_dist + 1

                    path_lens[current_id] = current_dist
                else:
                    diff_x = diff_x - 1
                    routing[current_id, direct_x] = 1
                    current_id = self.chip_matrix[current_id].neighbor_chips[direct_x].id
                    src_set.append(current_id)
                    current_dist = current_dist + 1
                    path_lens[current_id] = current_dist
            routing[current_id, DIRECTION.LOCAL] = 1
            routing_record.append(routing)
            if filted_dst_cand == current_id:
                dst_set.remove(current_id)
            else:
                logger.error(
                    f'routing final_id {current_id} is not equal to dst_id {filted_dst_cand}')
                exit(1)
            src_set = list(set(src_set))
            # src_set = sorted(src_set)
            # logger.info(f'src_set: {src_set}')
            # logger.info(f'dst_set: {dst_set}')
            # logger.info(f'path_len: {path_lens}')
        # logger.info(
        #     f'\n\n===================Finish Non-Straight Forward===================')
        # logger.info(f'routing_record: \n{np.array(routing)}')

        # updata router_load
        for chip_id in range(self.TotalChips):
            route_info = routing[chip_id]
            if np.sum(route_info) == 0:
                continue
            for direct in FIVE_DIRECTION:
                self.router_load[chip_id, direct] = self.router_load[chip_id,
                                                                     direct] + routing[chip_id][direct]
        return routing

    def connection_into_npu_flow(self, connection_matrix):
        """_summary_

        Parameters
        ----------
        connection_matrix : dict
            connection_matrix[src_v] = [dst_v1, dst_v2, ...]

        """
        # vertex into npus/chips
        self.vertex_to_npus = []
        self.vertex_to_chips = []
        for i in range(self.neuron_num):
            npu_id = i // self.RouterGroupRange
            self.vertex_to_npus.append(npu_id)
            self.vertex_to_chips.append(self.npus_to_chips[npu_id])

        # edge to npu flow
        self.npu_flows_to_chips = {}
        for src_v in connection_matrix:
            for dst_v in connection_matrix[src_v]:
                src_npu = self.vertex_to_npus[src_v]
                dst_chip = self.vertex_to_chips[dst_v]
                if src_npu in self.npu_flows_to_chips:
                    self.npu_flows_to_chips[src_npu].append(dst_chip)
                else:
                    self.npu_flows_to_chips[src_npu] = [dst_chip]

        for src_npu in self.npu_flows_to_chips:
            self.npu_flows_to_chips[src_npu] = list(
                set(self.npu_flows_to_chips[src_npu]))
        self.npu_flows_to_chips = {key: self.npu_flows_to_chips[key] for key in sorted(self.npu_flows_to_chips)}
        
        if self.mode == 2:
            nTile = self.X_NumOfChips*self.Y_NumOfChips
            split = int(nTile/2)
            for key, values in self.npu_flows_to_chips.items():
                transformed_list = list(set(value - split if value >= split else value for value in values))
                self.npu_flows_to_chips[key] = transformed_list

            self.npus_to_chips = list(value - split if value >= split else value for value in self.npus_to_chips)
        
        self.log = ["-----------Router-----------\n"]
        self.log.append(f'X_NumOfChips_used: {self.X_NumOfChips}\n')
        self.log.append(f'Y_NumOfChips_used: {self.Y_NumOfChips}\n')
        self.log.append(f'Is_Y_First: {self.Is_Y_First}\n')
        self.log.append(f'RouterGroupRange: {self.RouterGroupRange}\n')
        self.log.append(f'Router_GroupNum: {self.NodeNumOfNpu}\n')
        self.log.append(f'npu_flows_to_chips: \n')
        for i in self.npu_flows_to_chips:
            self.log.append(f'\tp{i}: {self.npu_flows_to_chips[i]}\n')

        return self.npu_flows_to_chips

    def gen_routing(self, connection_matrix):
        self.connection_into_npu_flow(connection_matrix)
        route_path = []
        for src_npu in range(self.npu_num):
            if src_npu in self.npu_flows_to_chips:
                src_chip = self.npus_to_chips[src_npu]
                dst_chip = self.npu_flows_to_chips[src_npu]
                routing = self.get_one_src_routing(
                    src_chip, dst_chip)
                route_path.append(routing)
            else:
                route_path.append(np.zeros((self.TotalChips, 5)))
        self.route_path = np.array(route_path)

        return self.route_path


class Router40nm(Router):
    def __init__(self, config, neuron_num) -> None:
        super().__init__(config, neuron_num)
        self.bram_depth = 1024
        self.bram_num = 16

        self.direction_weight = [8, 4, 2, 1, 16]

    def get_bram_index(self, npu_id):
        bram_col = self.bram_num - int(npu_id / self.bram_depth) - 1
        bram_row = npu_id % self.bram_depth
        bram_index = bram_row * self.bram_num + bram_col

        return bram_index

    def write_to_bin(self, save_dir):
        save_dir = Path(save_dir) / 'route_info'
        save_dir.mkdir(parents=True, exist_ok=True)

        # 第一位使能为1
        route_enable = (np.sum(self.route_path, axis=2)
                        > 0).astype("<u2") * (2**15)
        route_tag = np.tile(
            (np.floor(np.mod(np.arange(self.npu_num),
                             (2**20)) / (2**10)) * (2**5)).astype("<u2"),
            (self.TotalChips, 1),
        ).T
        self.route_info = (
            route_enable
            + route_tag
            + self.route_path[:, :, DIRECTION.LOCAL].astype(
                "<u2") * self.direction_weight[DIRECTION.LOCAL]
            + self.route_path[:, :, DIRECTION.WEST].astype(
                "<u2") * self.direction_weight[DIRECTION.WEST]
            + self.route_path[:, :, DIRECTION.SOUTH].astype(
                "<u2") * self.direction_weight[DIRECTION.SOUTH]
            + self.route_path[:, :, DIRECTION.EAST].astype(
                "<u2") * self.direction_weight[DIRECTION.EAST]
            + self.route_path[:, :, DIRECTION.NORTH].astype(
                "<u2") * self.direction_weight[DIRECTION.NORTH]
        )

        for n in range(self.route_info.shape[1]):
            file_path = save_dir / f'route_info_{n}.bin'
            file_path.unlink(missing_ok=True)
            data = np.zeros((self.bram_depth * self.bram_num, 1), "uint16")
            for i in range(self.route_info.shape[0]):
                data[self.get_bram_index(i)] = self.route_info[i, n]
            Fake.fwrite(file_path=file_path, arr=data, dtype="<u2")


class lb2_Router(Router):
    def __init__(self, config, neuron_num, mode=0) -> None:
        super().__init__(config, neuron_num)
        self.bram_depth = 4096 
        self.bram_num = 4 #nBlock in a row
        self.bram_block_depth = 1024 #nRow
        self.bram_block_count = self.bram_num * self.bram_block_depth
        self.mode = mode
        self.direction_weight = [2, 4, 1, 8, 16]

    def get_bram_index(self, npu_id):
        bram_block = int(npu_id / self.bram_block_count)
        block_id = int(npu_id % self.bram_block_count)
        bram_col = self.bram_num - \
            int(block_id / self.bram_block_depth) - 1
        bram_row = block_id % self.bram_block_depth + bram_block * self.bram_block_depth
        bram_index = bram_row * self.bram_num + bram_col

        return bram_index

    def bin_reshape(self, data: np.ndarray):
        return np.flip(data.reshape(-1, 4), axis=1).reshape(-1, 1)

    def write_to_bin(self, save_dir, file_type='bin'):
        save_dir = Path(save_dir) / 'route_info' if file_type=='bin' else Path(save_dir) /'hex' / 'route_info'
        save_dir.mkdir(parents=True, exist_ok=True)

        # 第一位使能为1
        route_enable = (np.sum(self.route_path, axis=2)
                        > -1).astype("<u2") * (2**15)
        route_tag = np.tile(
            (np.floor(np.mod(np.arange(self.npu_num),
                             (2**20)) / (2**10)) * (2**5)).astype("<u2"),
            (self.TotalChips, 1),
        ).T
        self.route_info = (
            route_enable
            + route_tag
            + self.route_path[:, :, DIRECTION.LOCAL].astype(
                "<u2") * self.direction_weight[DIRECTION.LOCAL]
            + self.route_path[:, :, DIRECTION.WEST].astype(
                "<u2") * self.direction_weight[DIRECTION.WEST]
            + self.route_path[:, :, DIRECTION.SOUTH].astype(
                "<u2") * self.direction_weight[DIRECTION.SOUTH]
            + self.route_path[:, :, DIRECTION.EAST].astype(
                "<u2") * self.direction_weight[DIRECTION.EAST]
            + self.route_path[:, :, DIRECTION.NORTH].astype(
                "<u2") * self.direction_weight[DIRECTION.NORTH]
        )
        for n in range(self.route_info.shape[1]):
            if file_type == 'hex':
                file_path = save_dir / f'route_info_{n}.hex'
            else:
                file_path = save_dir / f'route_info_{n}.bin'
            file_path.unlink(missing_ok=True)
            data = np.zeros((self.bram_depth * self.bram_num, 1), "uint16")
            for i in range(self.route_info.shape[0]):
                data[self.get_bram_index(i)] = self.route_info[i, n]

            if file_type == 'hex':
                hex_file = array_to_hex(data)
                save_hex_file(file_path, hex_file, each_row_num=16)
            else:
                Fake.fwrite(file_path=file_path,
                            arr=self.bin_reshape(data), dtype="<u2")
