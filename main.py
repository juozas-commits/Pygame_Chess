import pygame
import sys
import math

pygame.init()
WHITE_TOP_ROW = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
WHITE_DOUBLE_ROW = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)]
BLACK_TOP_ROW = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
BLACK_DOUBLE_ROW = [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)]

clock = pygame.time.Clock()
screen_width = 1080
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SACHMATAI")

black_colour = (64, 62, 68)
white_colour = (127, 124, 133)

chess_board = pygame.image.load(f'Directory\\chess_board.png')

black_check_mate = False
white_check_mate = False

check_mate = pygame.image.load(f'Directory\\check_mate.png')


def get_cords():
    return math.floor(x_mouse/135), math.floor(y_mouse/135)


class ChoosingBoard:
    def __init__(self, team):
        if team == 1:
            self.image = pygame.image.load(f'Directory\\white_choosing_board.png')
            self.rect = self.image.get_rect(topleft=(135, 135))
        else:
            self.image = pygame.image.load(f'Directory\\black_choosing_board.png')
            self.rect = self.image.get_rect(topleft=(270, 810))


class ChoosingBoardOmni:
    def __init__(self, team):
        if team == 1:
            self.image = pygame.image.load(f'Directory\\white_choosing_board_omni.png')
            self.rect = self.image.get_rect(topleft=(135, 135))
        else:
            self.image = pygame.image.load(f'Directory\\black_choosing_board_omni.png')
            self.rect = self.image.get_rect(topleft=(270, 810))


class TileChooser:
    def __init__(self):
        self.x, self.y = get_cords()
        self.image = pygame.image.load(f'Directory\\tile_chooser.png')
        self.rect = self.image.get_rect(topleft=(self.x * 135, self.y * 135))


class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, coords):
        self.coordinates = x, y = coords
        self.offset_x, self.offset_y = coords
        self.rect.topleft = [(135 * x) + 7.5, (135 * y) + 7.5]

    def track(self):
        self.rect.topleft = [x_mouse - 60, y_mouse - 60]


class King(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\king_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\king_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]
        self.can_castle = True

        self.legal_moves = []


class Queen(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\queen_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\queen_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]

        self.legal_moves = []


class Rook(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\rook_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\rook_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]
        self.havent_moved = True
        self.legal_moves = []


class Knight(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\knight_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\knight_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]

        self.legal_moves = []


class Bishop(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\bishop_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\bishop_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]

        self.legal_moves = []


class Pawn(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\pawn_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\pawn_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]
        self.can_move_two = True

        self.can_capture_en_pasant = False
        self.can_capture_en_pasant_on = ()
        self.can_be_captured_en_pasant = False

        self.legal_moves = []


class Omni(Piece):
    def __init__(self, piece_name, team, offset):
        super().__init__()
        self.name = f'{piece_name}'
        self.team = team
        self.offset_x, self.offset_y = self.coordinates = offset
        self.image = pygame.Surface([120, 120])
        if self.team == -1:
            self.image = pygame.image.load(f'Directory\\omni_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\omni_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]

        self.legal_moves = []

king_black = King('king_black', -1, (4, 0))
queen_black = Queen('queen_black', -1, (3, 0))
rook_black_left = Rook('rook_black_l', -1, (0, 0))
rook_black_right = Rook('rook_black_r', -1, (7, 0))
knight_black_left = Knight('knight_black_l', -1, (1, 0))
knight_black_right = Knight('knight_black_r', -1, (6, 0))
bishop_black_left = Bishop('bishop_black_l', -1, (2, 0))
bishop_black_right = Bishop('bishop_black_r', -1, (5, 0))
pawn_black_a = Pawn('pawn_black_h', -1, (0, 1))
pawn_black_b = Pawn('pawn_black_g', -1, (1, 1))
pawn_black_c = Pawn('pawn_black_f', -1, (2, 1))
pawn_black_d = Pawn('pawn_black_e', -1, (3, 1))
pawn_black_e = Pawn('pawn_black_d', -1, (4, 1))
pawn_black_f = Pawn('pawn_black_c', -1, (5, 1))
pawn_black_g = Pawn('pawn_black_b', -1, (6, 1))
pawn_black_h = Pawn('pawn_black_a', -1, (7, 1))

king_white = King('king_white', 1, (4, 7))
queen_white = Queen('queen_white', 1, (3, 7))
rook_white_left = Rook('rook_white_l', 1, (0, 7))
rook_white_right = Rook('rook_white_r', 1, (7, 7))
knight_white_left = Knight('knight_white_l', 1, (1, 7))
knight_white_right = Knight('knight_white_r', 1, (6, 7))
bishop_white_left = Bishop('bishop_white_l', 1, (2, 7))
bishop_white_right = Bishop('bishop_white_r', 1, (5, 7))
pawn_white_a = Pawn('pawn_white_h', 1, (0, 6))
pawn_white_b = Pawn('pawn_white_g', 1, (1, 6))
pawn_white_c = Pawn('pawn_white_f', 1, (2, 6))
pawn_white_d = Pawn('pawn_white_e', 1, (3, 6))
pawn_white_e = Pawn('pawn_white_d', 1, (4, 6))
pawn_white_g = Pawn('pawn_white_b', 1, (6, 6))
pawn_white_f = Pawn('pawn_white_c', 1, (5, 6))
pawn_white_h = Pawn('pawn_white_a', 1, (7, 6))

all_pieces_sprite_group = pygame.sprite.Group()
all_pawns = pygame.sprite.Group()
white_pawns = pygame.sprite.Group()
black_pawns = pygame.sprite.Group()

queens = pygame.sprite.Group()
black_queens = pygame.sprite.Group()
white_queens = pygame.sprite.Group()

rooks = pygame.sprite.Group()
black_rooks = pygame.sprite.Group()
white_rooks = pygame.sprite.Group()

bishops = pygame.sprite.Group()
black_bishops = pygame.sprite.Group()
white_bishops = pygame.sprite.Group()

knights = pygame.sprite.Group()
black_knights = pygame.sprite.Group()
white_knights = pygame.sprite.Group()

omnis = pygame.sprite.Group()

kings = pygame.sprite.Group()

all_pieces_sprite_group.add(queen_black, rook_black_left, rook_black_right, knight_black_left, knight_black_right, bishop_black_left, bishop_black_right,
                            pawn_black_h, pawn_black_g, pawn_black_f, pawn_black_e, pawn_black_d, pawn_black_c, pawn_black_b, pawn_black_a,
                            queen_white, rook_white_left, rook_white_right, knight_white_left, knight_white_right, bishop_white_left, bishop_white_right,
                            pawn_white_h, pawn_white_g, pawn_white_f, pawn_white_e, pawn_white_d, pawn_white_c, pawn_white_b, pawn_white_a, king_black, king_white)

all_pawns.add(pawn_black_h, pawn_black_g, pawn_black_f, pawn_black_e, pawn_black_d, pawn_black_c, pawn_black_b, pawn_black_a,
              pawn_white_h, pawn_white_g, pawn_white_f, pawn_white_e, pawn_white_d, pawn_white_c, pawn_white_b, pawn_white_a)
white_pawns.add(pawn_white_h, pawn_white_g, pawn_white_f, pawn_white_e, pawn_white_d, pawn_white_c, pawn_white_b, pawn_white_a)
black_pawns.add(pawn_black_h, pawn_black_g, pawn_black_f, pawn_black_e, pawn_black_d, pawn_black_c, pawn_black_b, pawn_black_a)

queens.add(queen_white, queen_black)
black_queens.add(queen_black)
white_queens.add(queen_white)

rooks.add(rook_white_left, rook_white_right, rook_black_left, rook_black_right)
black_rooks.add(rook_black_left, rook_black_right)
white_rooks.add(rook_white_left, rook_white_right)

bishops.add(bishop_white_left, bishop_white_right, bishop_black_left, bishop_black_right)
black_bishops.add(bishop_black_left, bishop_black_right)
white_bishops.add(bishop_white_left, bishop_white_right)

knights.add(knight_white_left, knight_white_right, knight_black_left, knight_black_right)
black_knights.add(knight_black_left, knight_black_right)
white_knights.add(knight_white_left, knight_white_right)

kings.add(king_black, king_white)

black_pieces_defending_list = []
white_pieces_defending_list = []

black_pieces_position_list = []
white_pieces_position_list = []

black_threatening_moves = []
white_threatening_moves = []


def update_black_pieces_positions():
    black_pieces_position_list.clear()
    for piece_black in all_pieces_sprite_group:
        if piece_black.team == -1:
            black_pieces_position_list.append((piece_black.offset_x, piece_black.offset_y))


def update_white_pieces_positions():
    white_pieces_position_list.clear()
    for piece_white in all_pieces_sprite_group:
        if piece_white.team == 1:
            white_pieces_position_list.append((piece_white.offset_x, piece_white.offset_y))


def check_if_coordinates_in_enemy_team(pieces_in_question, inner_offset_x, inner_offset_y):
    cords = (inner_offset_x, inner_offset_y)
    is_it_in = False
    if pieces_in_question == 1:
        if cords in black_pieces_position_list:
            is_it_in = True
    if pieces_in_question == -1:
        if cords in white_pieces_position_list:
            is_it_in = True
    return is_it_in


def check_if_coordinates_in_native_team(pieces_in_question, inner_offset_x, inner_offset_y):
    cords = (inner_offset_x, inner_offset_y)
    is_it_in = False
    if pieces_in_question == 1:
        if cords in white_pieces_position_list:
            is_it_in = True
    if pieces_in_question == -1:
        if cords in black_pieces_position_list:
            is_it_in = True
    return is_it_in


def update_black_threatening_moves():
    for black_piece in all_pieces_sprite_group:
        if black_piece.team == -1 and not black_piece in all_pawns:
            for cord in black_piece.legal_moves:
                black_threatening_moves.append(cord)


def update_white_threatening_moves():
    for white_piece in all_pieces_sprite_group:
        if white_piece.team == 1 and not white_piece in all_pawns:
            for cord in white_piece.legal_moves:
                white_threatening_moves.append(cord)


def check_if_castling_left_allowed_for_black():
    if rook_black_left in all_pieces_sprite_group and rook_black_left.havent_moved and king_black.can_castle:
        king_black_can_castle = True
        for move in white_threatening_moves:
            if (move == (2, 0)) or (move == (3, 0)) or (move == (4, 0)):
                king_black_can_castle = False
        for move1 in white_pieces_position_list:
            if (move1 == (1, 0)) or (move1 == (2, 0)) or (move1 == (3, 0)):
                king_black_can_castle = False
        for move2 in black_pieces_position_list:
            if (move2 == (1, 0)) or (move2 == (2, 0)) or (move2 == (3, 0)):
                king_black_can_castle = False
    else:
        king_black_can_castle = False
    return king_black_can_castle


def check_if_castling_right_allowed_for_black():
    if rook_black_right in all_pieces_sprite_group and rook_black_right.havent_moved and king_black.can_castle:
        king_black_can_castle = True
        for move in white_threatening_moves:
            if (move == (4, 0)) or (move == (5, 0)) or (move == (6, 0)):
                king_black_can_castle = False
        for move1 in white_pieces_position_list:
            if (move1 == (5, 0)) or (move1 == (6, 0)):
                king_black_can_castle = False
        for move2 in black_pieces_position_list:
            if (move2 == (5, 0)) or (move2 == (6, 0)):
                king_black_can_castle = False
    else:
        king_black_can_castle = False
    return king_black_can_castle


def check_if_castling_left_allowed_for_white():
    if rook_white_left in all_pieces_sprite_group and rook_white_left.havent_moved and king_white.can_castle:
        king_white_can_castle = True
        for move in black_threatening_moves:
            if (move == (2, 7)) or (move == (3, 7)) or (move == (4, 7)):
                king_white_can_castle = False
        for move1 in white_pieces_position_list:
            if (move1 == (1, 7)) or (move1 == (2, 7)) or (move1 == (3, 7)):
                king_white_can_castle = False
        for move2 in black_pieces_position_list:
            if (move2 == (1, 7)) or (move2 == (2, 7)) or (move2 == (3, 7)):
                king_white_can_castle = False
    else:
        king_white_can_castle = False
    return king_white_can_castle


def check_if_castling_right_allowed_for_white():
    if rook_white_right in all_pieces_sprite_group and rook_white_right.havent_moved and king_white.can_castle:
        king_white_can_castle = True
        for move in black_threatening_moves:
            if (move == (4, 7)) or (move == (5, 7)) or (move == (6, 7)):
                king_white_can_castle = False
        for move1 in white_pieces_position_list:
            if (move1 == (5, 7)) or (move1 == (6, 7)):
                king_white_can_castle = False
        for move2 in black_pieces_position_list:
            if (move2 == (5, 7)) or (move2 == (6, 7)):
                king_white_can_castle = False
    else:
        king_white_can_castle = False
    return king_white_can_castle


def kings_legal_moves():

    update_black_threatening_moves()
    update_white_threatening_moves()
    for king in kings:
        if king.can_castle:
            if king.team == 1:
                if check_if_castling_left_allowed_for_white():
                    king.legal_moves.append((2, 7))
                if check_if_castling_right_allowed_for_white():
                    king.legal_moves.append((6, 7))
            else:
                if check_if_castling_left_allowed_for_black():
                    king.legal_moves.append((2, 0))
                if check_if_castling_right_allowed_for_black():
                    king.legal_moves.append((6, 0))

    w_substracted = []
    for move in king_white.legal_moves:
        if move not in black_pieces_defending_list and move not in black_threatening_moves:
            w_substracted.append(move)
    king_white.legal_moves = w_substracted

    b_substracted = []
    for move in king_black.legal_moves:
        if move not in white_pieces_defending_list and move not in white_threatening_moves:
            b_substracted.append(move)
    king_black.legal_moves = b_substracted


def black_king_is_in_check():
    black_king_is_in_check = False
    for cord in white_threatening_moves:
        if king_black.coordinates == cord:
            black_king_is_in_check = True
    return black_king_is_in_check


def white_king_is_in_check():
    white_king_is_in_check = False
    for cord in black_threatening_moves:
        if king_white.coordinates == cord:
            white_king_is_in_check = True
    return white_king_is_in_check


def adjusted_for_check(team):

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x >= 0 and not breaking:
        king_x -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0:
                    king_x -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_rooks or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0:
                    king_x -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_rooks or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x <= 7 and not breaking:
        king_x += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7:
                    king_x += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_rooks or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7:
                    king_x += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_rooks or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_y >= 0 and not breaking:
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_y >= 0:
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_rooks or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break

        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_y >= 0:
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_rooks or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_y <= 7 and not breaking:
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_y <= 7:
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_rooks or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_y <= 7:
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_rooks or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x <= 7 and king_y <= 7 and not breaking:
        king_x += 1
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7 and king_y <= 7:
                    king_x += 1
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_bishops or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7 and king_y <= 7:
                    king_x += 1
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_bishops or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x >= 0 and king_y >= 0 and not breaking:
        king_x -= 1
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0 and king_y >= 0:
                    king_x -= 1
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_bishops or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0 and king_y >= 0:
                    king_x -= 1
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_bishops or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x >= 0 and king_y <= 7 and not breaking:
        king_x -= 1
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0 and king_y <= 7:
                    king_x -= 1
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_bishops or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x >= 0 and king_y <= 7:
                    king_x -= 1
                    king_y += 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_bishops or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in white_pieces_position_list:
                        breaking = True
                        break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    breaking = False

    while king_x <= 7 and king_y >= 0 and not breaking:
        king_x += 1
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in black_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7 and king_y >= 0:
                    king_x += 1
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in white_bishops or piece in white_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break
        if team == 1:
            if (king_x, king_y) in white_pieces_position_list:
                cant_be_moved = True
                piece_that_cant_move = (king_x, king_y)
                while cant_be_moved and king_x <= 7 and king_y >= 0:
                    king_x += 1
                    king_y -= 1
                    w_substract_while_checks_internal.append((king_x, king_y))
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and (
                                    piece in black_bishops or piece in black_queens):
                                for piece_that_restricted in all_pieces_sprite_group:
                                    if piece_that_restricted.coordinates == piece_that_cant_move:
                                        b_sub = []
                                        for move in piece_that_restricted.legal_moves:
                                            if move in w_substract_while_checks_internal:
                                                b_sub.append(move)
                                        piece_that_restricted.legal_moves = b_sub
                                        cant_be_moved = False
                                        breaking = True
                                        break
                    if (king_x, king_y) in black_pieces_position_list:
                        breaking = True
                        break


def substract_for_checks(team):
    w_substract_while_check = []

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 0:
        king_x -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_rooks or piece in white_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_rooks or piece in black_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 7:
        king_x += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_rooks or piece in white_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_rooks or piece in black_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_y != 0:
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_rooks or piece in white_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_rooks or piece in black_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_y != 7:
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_rooks or piece in white_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_rooks or piece in black_queens):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 0 and king_y != 0:
        king_x -= 1
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_bishops or piece in white_queens or piece in white_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_bishops or piece in black_queens or piece in black_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 7 and king_y != 7:
        king_x += 1
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_bishops or piece in white_queens or piece in white_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_bishops or piece in black_queens or piece in black_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []
    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 7 and king_y != 0:
        king_x += 1
        king_y -= 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_bishops or piece in white_queens or piece in white_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_bishops or piece in black_queens or piece in black_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    w_substract_while_checks_internal = []

    if team == -1:
        king_x, king_y = king_black.coordinates
    else:
        king_x, king_y = king_white.coordinates

    while king_x != 0 and king_y != 7:
        king_x -= 1
        king_y += 1
        w_substract_while_checks_internal.append((king_x, king_y))
        if team == -1:
            if (king_x, king_y) in white_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in white_bishops or piece in white_queens or piece in white_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in black_pieces_position_list:
                break
        else:
            if (king_x, king_y) in black_pieces_position_list:
                for piece in all_pieces_sprite_group:
                    if piece.coordinates == (king_x, king_y) and (piece in black_bishops or piece in black_queens or piece in black_pawns):
                        w_substract_while_check.extend(w_substract_while_checks_internal)
            if (king_x, king_y) in white_pieces_position_list:
                break

    for n in range(2):
        for i in range(2):
            for j in range(2):
                if team == -1:
                    king_x, king_y = king_black.coordinates
                else:
                    king_x, king_y = king_white.coordinates
                a = 2 * pow(-1, i)
                b = 1 * pow(-1, j)
                if n == 0:
                    king_x += a
                    king_y += b
                else:
                    king_x += b
                    king_y += a

                if team == -1:
                    if (king_x, king_y) in white_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and piece in white_knights:
                                w_substract_while_check.append((king_x, king_y))
                else:
                    if (king_x, king_y) in black_pieces_position_list:
                        for piece in all_pieces_sprite_group:
                            if piece.coordinates == (king_x, king_y) and piece in black_knights:
                                w_substract_while_check.append((king_x, king_y))

    if team == -1:
        for all_black_piece in all_pieces_sprite_group:
            if all_black_piece not in kings and all_black_piece.team == team:
                b_sub = []
                for legal_move in all_black_piece.legal_moves:
                    if legal_move in w_substract_while_check:
                        b_sub.append(legal_move)
                all_black_piece.legal_moves = b_sub

    else:
        for all_white_piece in all_pieces_sprite_group:
            if all_white_piece not in kings and all_white_piece.team == team:
                b_sub = []
                for legal_move in all_white_piece.legal_moves:
                    if legal_move in w_substract_while_check:
                        b_sub.append(legal_move)
                all_white_piece.legal_moves = b_sub


def calculate_legal_moves():
    update_white_pieces_positions()
    update_black_pieces_positions()

    black_pieces_defending_list.clear()
    white_pieces_defending_list.clear()

    black_threatening_moves.clear()
    white_threatening_moves.clear()

    for all_piece in all_pieces_sprite_group:
        all_piece.legal_moves.clear()

        if all_piece in omnis:
            for i in range(8):
                for j in range(8):
                    all_piece.legal_moves.append((i, j))
            all_piece.legal_moves.remove(all_piece.coordinates)

        if all_piece in all_pawns:
            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if all_piece.team == -1:
                piece_offset_y += 1
            else:
                piece_offset_y -= 1
            if not check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                    check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if all_piece.can_move_two:
                    if all_piece.team == -1:
                        piece_offset_y += 1
                    else:
                        piece_offset_y -= 1
                    if not check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                            check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                        all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                        if all_piece.team == -1:
                            all_piece.legal_moves.append((piece_offset_x, 3))
                            piece_offset_y -= 1
                        else:
                            all_piece.legal_moves.append((piece_offset_x, 4))
                            piece_offset_y += 1
                    else:
                        if all_piece.team == -1:
                            piece_offset_y -= 1
                        else:
                            piece_offset_y += 1

            for i in range(2):
                piece_offset_x -= 1 + (-3 * i)
                if all_piece.team == 1:
                    white_threatening_moves.append((piece_offset_x, piece_offset_y))
                else:
                    black_threatening_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))

            if all_piece.can_capture_en_pasant:
                all_piece.legal_moves.append(all_piece.can_capture_en_pasant_on)

        if all_piece in rooks:
            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0:
                piece_offset_x -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7:
                piece_offset_x += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_y != 0:
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_y != 7:
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                        break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

        if all_piece in bishops:
            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0 and piece_offset_y != 0:
                piece_offset_x -= 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7 and piece_offset_y != 7:
                piece_offset_x += 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7 and piece_offset_y != 0:
                piece_offset_x += 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0 and piece_offset_y != 7:
                piece_offset_x -= 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

        if all_piece in knights:
            for n in range (2):
                for i in range(2):
                    for j in range(2):
                        piece_offset_x = all_piece.offset_x
                        piece_offset_y = all_piece.offset_y
                        a = 2 * pow(-1, i)
                        b = 1 * pow(-1, j)
                        if n == 0:
                            piece_offset_x += a
                            piece_offset_y += b
                        else:
                            piece_offset_x += b
                            piece_offset_y += a
                        if ((0 <= piece_offset_x <= 7) and (0 <= piece_offset_y <= 7)):
                            if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                                if all_piece.team == 1:
                                    white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                                else:
                                    black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                            else:
                                all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

        if all_piece in queens:
            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0:
                piece_offset_x -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7:
                piece_offset_x += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_y != 0:
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_y != 7:
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0 and piece_offset_y != 0:
                piece_offset_x -= 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7 and piece_offset_y != 7:
                piece_offset_x += 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 7 and piece_offset_y != 0:
                piece_offset_x += 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y -= 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x += 1
                            piece_offset_y -= 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            while piece_offset_x != 0 and piece_offset_y != 7:
                piece_offset_x -= 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        if not (piece_offset_x, piece_offset_y) == king_black.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y += 1
                            white_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                    if all_piece.team == -1:
                        if not (piece_offset_x, piece_offset_y) == king_white.coordinates:
                            all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                            break
                        else:
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            piece_offset_x -= 1
                            piece_offset_y += 1
                            black_threatening_moves.append((piece_offset_x, piece_offset_y))
                            break
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    break
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

        if all_piece == king_white or all_piece == king_black:
            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 0:
                piece_offset_x -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 7:
                piece_offset_x += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_y != 0:
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_y != 7:
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 0 and piece_offset_y != 0:
                piece_offset_x -= 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 7 and piece_offset_y != 7:
                piece_offset_x += 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 7 and piece_offset_y != 0:
                piece_offset_x += 1
                piece_offset_y -= 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

            piece_offset_x = all_piece.offset_x
            piece_offset_y = all_piece.offset_y
            if piece_offset_x != 0 and piece_offset_y != 7:
                piece_offset_x -= 1
                piece_offset_y += 1
                if check_if_coordinates_in_enemy_team(all_piece.team, piece_offset_x, piece_offset_y) and not \
                        check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))
                if check_if_coordinates_in_native_team(all_piece.team, piece_offset_x, piece_offset_y):
                    if all_piece.team == 1:
                        white_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                    else:
                        black_pieces_defending_list.append((piece_offset_x, piece_offset_y))
                else:
                    all_piece.legal_moves.append((piece_offset_x, piece_offset_y))

    kings_legal_moves()

    adjusted_for_check(turn * -1)

    if black_king_is_in_check() :
        substract_for_checks(-1)

    if white_king_is_in_check():
        substract_for_checks(1)

mouse_is_pressed = False
name_of_held_piece = ''

turn = 1
counter = 0

calculate_legal_moves()

while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_pressed = True

        if ev.type == pygame.MOUSEBUTTONUP:
            mouse_is_pressed = False

    screen.blit(chess_board, pygame.rect.Rect(0, 0, 1080, 1080))

    x_mouse, y_mouse = pygame.mouse.get_pos()
    x_cord, y_cord = get_cords()

    tile = TileChooser()
    screen.blit(tile.image, tile.rect)

    for piece in all_pieces_sprite_group:

        # Checks if the mouse coordinates are above the piece and if so, are we clicking the left button,
        # then takes the name of that piece to later track on mouse.
        # Additional conditions are NO piece has to be held at the time and there has to be a Turn of that team.
        if (piece.rect.left <= x_mouse <= piece.rect.right) and \
                (piece.rect.top <= y_mouse <= piece.rect.bottom) \
                and mouse_is_pressed and name_of_held_piece == '' and piece.team == turn:
            name_of_held_piece = piece.name

        # Tracks the piece Sprite to mouse pointer. Does not change the coordinates atribute.
        if name_of_held_piece == piece.name:
            piece.track()
            pygame.mouse.set_visible(False)
            for move in piece.legal_moves:
                x, y = move
                x = x * 135 + 67.5
                y = y * 135 + 67.5
                pygame.draw.circle(screen, (150, 38, 28), (x, y), 20, 20)

        # Activates if the piece was let go.
        if name_of_held_piece == piece.name and not mouse_is_pressed:

            # If the mouse let go of piece above the square that is in legal moves of this piece.
            if get_cords() in piece.legal_moves:
                backup_coordinates = piece.coordinates

                # Checks if there are Sprites in these coordinates and removes it.
                # Doesn't affect friendly team as that wouldn't be a Legal move

                if piece in all_pawns and piece.can_capture_en_pasant and piece.can_capture_en_pasant_on == get_cords():
                    for pawn_being_captured in all_pawns:
                        if pawn_being_captured.can_be_captured_en_pasant == True:
                            all_pieces_sprite_group.remove(pawn_being_captured)
                            all_pawns.remove(pawn_being_captured)
                            if pawn_being_captured.team == 1:
                                white_pawns.remove(pawn_being_captured)
                            else:
                                black_pawns.remove(pawn_being_captured)
                    piece.can_capture_en_pasant = False

                else:
                    for pawns in all_pawns:
                        pawns.can_be_captured_en_pasant = False
                        pawns.can_capture_en_pasant = False

                for captured_piece in all_pieces_sprite_group:
                    if get_cords() == captured_piece.coordinates:
                        all_pieces_sprite_group.remove(captured_piece)

                # Checks for castling is allowed
                if (piece == king_black and king_black.can_castle) or (piece == king_white and king_white.can_castle):

                    if piece == king_black and get_cords() == (2, 0):
                        piece.update(get_cords())
                        rook_black_left.update((3, 0))
                        rook_black_left.havent_moved = False

                    if piece == king_black and get_cords() == (6, 0):
                        piece.update(get_cords())
                        rook_black_right.update((5, 0))
                        rook_black_right.havent_moved = False

                    if piece == king_white and get_cords() == (2, 7):
                        piece.update(get_cords())
                        rook_white_left.update((3, 7))
                        rook_white_left.havent_moved = False

                    if piece == king_white and get_cords() == (6, 7):
                        piece.update(get_cords())
                        rook_white_right.update((5, 7))
                        rook_white_right.havent_moved = False

                # if not castling, updates position as usual

                if (piece in white_pawns and get_cords() in BLACK_TOP_ROW) or (
                        piece in black_pawns and get_cords() in WHITE_TOP_ROW):
                    piece.update(get_cords())
                    choosing = True
                    omni = False
                    pygame.mouse.set_visible(True)
                    while choosing:
                        x_mouse, y_mouse = pygame.mouse.get_pos()
                        for ev in pygame.event.get():
                            pygame.display.flip()
                            if ev.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if ev.type == pygame.MOUSEBUTTONDOWN:
                                mouse_is_pressed = True
                            if ev.type == pygame.MOUSEBUTTONUP:
                                mouse_is_pressed = False

                        screen.blit(chess_board, pygame.rect.Rect(0, 0, 1080, 1080))
                        all_pieces_sprite_group.draw(screen)

                        choosing_screen = ChoosingBoard(piece.team)
                        choosing_screen_omni = ChoosingBoardOmni(piece.team)
                        tile_choosing = TileChooser()
                        screen.blit(tile_choosing.image, tile_choosing.rect)
                        pygame.draw.circle(screen, (150, 120, 0), (2, 405), 5, 20)

                        if (0 <= x_mouse <= 3) and (403 <= y_mouse <= 407) and mouse_is_pressed:
                            omni = True

                        if piece.team == 1:
                            if omni:
                                omni_white = pygame.image.load(f'Directory\\omni_white.png').convert_alpha()
                                screen.blit(choosing_screen_omni.image, choosing_screen_omni.rect)
                                screen.blit(omni_white, pygame.rect.Rect(682.5, 142.5, 120, 120))
                            else:
                                screen.blit(choosing_screen.image, choosing_screen_omni.rect)

                            screen.blit(queen_white.image, (547.5, 142.5))
                            screen.blit(rook_white_left.image, (413.5, 142.5))
                            screen.blit(bishop_white_left.image, (277.5, 142.5))
                            screen.blit(knight_white_left.image, (142.5, 142.5))

                            if get_cords() == (1, 1) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Knight(f"{counter}", 1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                knights.add(locals()[f'{counter}'])
                                white_knights.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (2, 1) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Bishop(f"{counter}", 1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                bishops.add(locals()[f'{counter}'])
                                white_bishops.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (3, 1) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Rook(f"{counter}", 1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                rooks.add(locals()[f'{counter}'])
                                white_rooks.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (4, 1) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Queen(f"{counter}", 1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                queens.add(locals()[f'{counter}'])
                                white_queens.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (5, 1) and mouse_is_pressed and omni:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Omni(f"{counter}", 1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                omnis.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False
                                turn *= -1

                        if piece.team == -1:
                            if omni:
                                omni_black = pygame.image.load(f'Directory\\omni_black.png').convert_alpha()
                                screen.blit(choosing_screen_omni.image, choosing_screen_omni.rect)
                                screen.blit(omni_black, pygame.rect.Rect(817.5, 817.5, 120, 120))
                            else:
                                screen.blit(choosing_screen.image, choosing_screen_omni.rect)

                            screen.blit(queen_black.image, (682.5, 817.5))
                            screen.blit(rook_black_left.image, (547.5, 817.5))
                            screen.blit(bishop_black_left.image, (412.5, 817.5))
                            screen.blit(knight_black_left.image, (277.5, 817.5))

                            if get_cords() == (2, 6) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Knight(f"{counter}", -1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                knights.add(locals()[f'{counter}'])
                                black_knights.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (3, 6) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Bishop(f"{counter}", -1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                bishops.add(locals()[f'{counter}'])
                                black_bishops.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (4, 6) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Rook(f"{counter}", -1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                rooks.add(locals()[f'{counter}'])
                                black_rooks.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (5, 6) and mouse_is_pressed:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Queen(f"{counter}", -1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                queens.add(locals()[f'{counter}'])
                                black_queens.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False

                            if get_cords() == (6, 6) and mouse_is_pressed and omni:
                                all_pieces_sprite_group.remove(piece)
                                locals()[f'{counter}'] = Omni(f"{counter}", -1, (piece.coordinates))
                                all_pieces_sprite_group.add(locals()[f'{counter}'])
                                omnis.add(locals()[f'{counter}'])
                                counter += 1
                                choosing = False
                                turn *= -1
                        clock.tick(60)

                if piece in black_pawns and piece.can_move_two and get_cords() in BLACK_DOUBLE_ROW:
                    piece.can_be_captured_en_pasant = True
                    for white_pawn in white_pawns:
                        if (white_pawn.offset_x == x_cord - 1 and white_pawn.offset_y == y_cord) or \
                                (white_pawn.offset_x == x_cord + 1 and white_pawn.offset_y == y_cord):
                            white_pawn.can_capture_en_pasant = True
                            white_pawn.can_capture_en_pasant_on = (x_cord, y_cord - 1)

                if piece in white_pawns and piece.can_move_two and get_cords() in WHITE_DOUBLE_ROW:
                    piece.can_be_captured_en_pasant = True
                    for black_pawn in black_pawns:
                        if (black_pawn.offset_x == x_cord - 1 and black_pawn.offset_y == y_cord) or \
                                (black_pawn.offset_x == x_cord + 1 and black_pawn.offset_y == y_cord):
                            black_pawn.can_capture_en_pasant = True
                            black_pawn.can_capture_en_pasant_on = (x_cord, y_cord + 1)

                # Check if the pieces moved is a King, Rook or a Pawn, if so they respectively lose Castling and Move per Two rights
                if piece == king_white or piece == king_black and piece.can_castle:
                    piece.can_castle = False

                if piece in all_pawns and piece.can_move_two:
                    piece.can_move_two = False

                if piece in rooks and piece.havent_moved:
                    piece.havent_moved = False

                piece.update(get_cords())
                calculate_legal_moves()
                turn *= -1

            else:
                piece.update(piece.coordinates)
            # Ends the sequence
            pygame.mouse.set_visible(True)
            name_of_held_piece = ''

    if black_king_is_in_check():
        black_check_mate = True
        for piece in all_pieces_sprite_group:
            if piece.team == -1 and piece.legal_moves != []:
                black_check_mate = False
        if king_black.legal_moves != []:
            black_check_mate = False

    if white_king_is_in_check():
        white_check_mate = True
        for piece in all_pieces_sprite_group:
            if piece.team ==  1 and piece.legal_moves != []:
                white_check_mate = False
        if king_white.legal_moves != []:
            white_check_mate = False

    while black_check_mate or white_check_mate:
        for ev in pygame.event.get():
            pygame.display.flip()
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(chess_board, pygame.rect.Rect(0, 0, 1080, 1080))
        all_pieces_sprite_group.draw(screen)
        screen.blit(check_mate, pygame.rect.Rect(100, 0, 1080, 1080))
        pygame.display.flip()
        clock.tick(60)


    all_pieces_sprite_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
