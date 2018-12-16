import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(ai_settings, alien_width):
    '''Get number of aliens for screen size'''
    available_space_x = int(ai_settings.screen_width - 2 * alien_width)
    num_aliens_x = int(available_space_x / (2 * alien_width))

    return num_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Get number of rows fitting the screen'''
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    num_rows = int(available_space_y / (2 * alien_height))

    return num_rows



def create_alien(ai_settings, screen, aliens, alien_number, num_row):
    '''Create a single alien'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * num_row

    alien.rect.x = alien.x
    alien.rect.y = alien.y

    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''Create a full fleet of aliens'''
    alien = Alien(ai_settings, screen)
    num_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    num_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


    #Create the fleet
    for num_row in range(num_rows):
        for alien_number in range(num_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, num_row)

def update_aliens(aliens):
    aliens.update()