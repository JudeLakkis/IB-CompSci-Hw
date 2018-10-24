def black_line(square_size, a):
    if (y / square_size) % 2 == 0:
        for i in range(5):
            x = 0
            for j in range(5):
                if (x / square_size) % 2 == 1:
                    pygame.draw.rect(screen, (255, 255, 255), ((x, y + a), (square_size, square_size)))
                    x += square_size
                elif (x / square_size) % 2 == 0:
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y + a), (square_size, square_size)))
                    x += square_size
    a += 50
    return a
