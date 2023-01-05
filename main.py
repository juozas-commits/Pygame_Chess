import pygame, sys, math


pygame.init()


def chessboard():
    screen.fill(black_colour)
    width = 135
    height = 135

    top = 0
    for y in range(8):
        if y % 2 == 0:
            left = 0
        else:
            left = 135
        for x in range(4):
            tile = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, white_colour, tile)
            left += 270
        top += 135


class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self, offset_x, offset_y, name_of_held_piece):
        self.rect.topleft = [135 * offset_x + 7.5, 135 * offset_y + 7.5]

    def track(self, offset_x, offset_y):
        self.rect.topleft = [offset_x - 60, offset_y - 60]

    def get_position(self):
        return self.rect.topleft


class King(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\king_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\king_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


class Queen(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\queen_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\queen_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


class Rook(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\rook_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\rook_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


class Knight(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\knight_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\knight_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


class Bishop(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\bishop_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\bishop_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


class Pawn(Piece):
    def __init__(self, piece_name, team, offset_x, offset_y):
        super().__init__()
        self.team = team
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.name = f'{piece_name}'
        self.image = pygame.Surface([120, 120])
        if self.team == 0:
            self.image = pygame.image.load(f'Directory\\pawn_black.png')
        if self.team == 1:
            self.image = pygame.image.load(f'Directory\\pawn_white.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [135*self.offset_x+7.5, 135*self.offset_y+7.5]


king_black = King('king_black', 0, 3, 7)
queen_black = Queen('queen_black', 0, 4, 7)
rook_black_left = Rook('rook_black_l', 0, 0, 7)
rook_black_right = Rook('rook_black_r', 0, 7, 7)
knight_black_left = Knight('knight_black_l', 0, 1, 7)
knight_black_right = Knight('knight_black_r', 0, 6, 7)
bishop_black_left = Bishop('bishop_black_l', 0, 2, 7)
bishop_black_right = Bishop('bishop_black_r', 0, 5, 7)

pawn_black_h = Pawn('pawn_black_h', 0, 0, 6)
pawn_black_g = Pawn('pawn_black_g', 0, 1, 6)
pawn_black_f = Pawn('pawn_black_f', 0, 2, 6)
pawn_black_e = Pawn('pawn_black_e', 0, 3, 6)
pawn_black_d = Pawn('pawn_black_d', 0, 4, 6)
pawn_black_c = Pawn('pawn_black_c', 0, 5, 6)
pawn_black_b = Pawn('pawn_black_b', 0, 6, 6)
pawn_black_a = Pawn('pawn_black_a', 0, 7, 6)

king_white = King('king_white', 1, 3, 0)
queen_white = Queen('queen_white', 1, 4, 0)
rook_white_left = Rook('rook_white_l', 1, 0, 0)
rook_white_right = Rook('rook_white_r', 1, 7, 0)
knight_white_left = Knight('knight_white_l', 1, 1, 0)
knight_white_right = Knight('knight_white_r', 1, 6, 0)
bishop_white_left = Bishop('bishop_white_l', 1, 2, 0)
bishop_white_right = Bishop('bishop_white_r', 1, 5, 0)

pawn_white_h = Pawn('pawn_white_h', 1, 0, 1)
pawn_white_g = Pawn('pawn_white_g', 1, 1, 1)
pawn_white_f = Pawn('pawn_white_f', 1, 2, 1)
pawn_white_e = Pawn('pawn_white_e', 1, 3, 1)
pawn_white_d = Pawn('pawn_white_d', 1, 4, 1)
pawn_white_c = Pawn('pawn_white_c', 1, 5, 1)
pawn_white_b = Pawn('pawn_white_b', 1, 6, 1)
pawn_white_a = Pawn('pawn_white_a', 1, 7, 1)

chess_pieces_sprite_group = pygame.sprite.Group()
chess_pieces_sprite_group.add(king_black, queen_black, rook_black_left, rook_black_right, knight_black_left, knight_black_right, bishop_black_left, bishop_black_right,
                              pawn_black_h, pawn_black_g, pawn_black_f, pawn_black_e, pawn_black_d, pawn_black_c, pawn_black_b, pawn_black_a,
                              king_white, queen_white, rook_white_left, rook_white_right, knight_white_left, knight_white_right, bishop_white_left, bishop_white_right,
                              pawn_white_h, pawn_white_g, pawn_white_f, pawn_white_e, pawn_white_d, pawn_white_c, pawn_white_b, pawn_white_a,)

clock = pygame.time.Clock()
screen_width = 1080
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SACHMATAI")

black_colour = (64, 62, 68)
white_colour = (127, 124, 133)

mouse_is_pressed = False
name_of_held_piece = ''

while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse_is_pressed = True
            pygame.mouse.set_visible(False)

        if ev.type == pygame.MOUSEBUTTONUP:
            mouse_is_pressed = False
            pygame.mouse.set_visible(True)

    chessboard()

    chess_pieces_sprite_group.draw(screen)

    x_mouse, y_mouse = pygame.mouse.get_pos()

    for piece in chess_pieces_sprite_group:
        if (piece.rect.left <= x_mouse <= piece.rect.right) and \
                (piece.rect.top <= y_mouse <= piece.rect.bottom) \
                and mouse_is_pressed and name_of_held_piece == '':
            name_of_held_piece = piece.name

        if name_of_held_piece == piece.name:
            piece.track(x_mouse, y_mouse)

        if name_of_held_piece == piece.name and not mouse_is_pressed:
            piece.update(math.floor(x_mouse/135), math.floor(y_mouse/135), name_of_held_piece)
            name_of_held_piece = ''

    pygame.display.flip()
    clock.tick(60)
