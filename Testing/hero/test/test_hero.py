from unittest import TestCase
from project.hero import Hero


class TestHero(TestCase):
    username = "Peter"
    level = 10
    health = 100
    damage = 10

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_enemy_hero_name_expect_exception(self):
        enemy = Hero("Peter", 10, 100, 10)
        with self.assertRaises(Exception) as msg:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(msg.exception))

    def test_if_hero_health_lt_0_before_battle(self):
        enemy = Hero("Sam", 10, 100, 10)
        self.hero.health = 0
        with self.assertRaises(Exception) as msg:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(msg.exception))

    def test_if_enemy_health_lt_0_before_battle(self):
        enemy = Hero("Sam", 10, 0, 10)
        with self.assertRaises(Exception) as msg:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Sam. He needs to rest", str(msg.exception))

    def test_hero_wins_battle(self):
        enemy = Hero("Sam", 5, 100, 10)
        msg = self.hero.battle(enemy)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(0, enemy.health)
        self.assertEqual(self.level+1, self.hero.level)
        self.assertEqual("You win", msg)

    def test_hero_loses(self):
        enemy = Hero("Sam", 10, 1000, 10)
        msg = self.hero.battle(enemy)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(905, enemy.health)
        self.assertEqual(11, enemy.level)
        self.assertEqual("You lose", msg)

    def test_heroes_draw_after_battle(self):
        enemy = Hero("Sam", 10, 100, 10)
        msg = self.hero.battle(enemy)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy.health)
        self.assertEqual("Draw", msg)

    def test_str_method(self):
        expected = f"Hero Peter: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 10\n"
        self.assertEqual(expected, str(self.hero))