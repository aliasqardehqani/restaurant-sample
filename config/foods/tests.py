from django.test import TestCase
from .models import Foods, Comment 

class FoodsModelTest(TestCase):
    def setUp(self):
        self.food = Foods.objects.create(
            food_name="کباب کوبیده",
            description="گوشت چرخ کرده گوسفندی",
            discount=10,
            rate=5,
            price=150000,
            photo="media/kabab.jpg",
            type_food="Lunch"
        )

    def test_food_creation(self):
        self.assertEqual(self.food.food_name, "کباب کوبیده")
        self.assertEqual(self.food.discount, 10)
        self.assertEqual(self.food.type_food, "Lunch")
        self.assertTrue(self.food.created)
        self.assertIn("کباب", str(self.food))

class CommentModelTest(TestCase):
    def setUp(self):
        self.food = Foods.objects.create(
            food_name="چلو مرغ",
            description="برنج ایرانی و ران مرغ",
            discount=0,
            rate=4,
            price=130000,
            photo="media/morgh.jpg",
            type_food="Lunch"
        )
        self.comment = Comment.objects.create(
            food=self.food,
            name="علی",
            email="ali@example.com",
            message="عالی بود"
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.name, "علی")
        self.assertEqual(self.comment.food, self.food)
        self.assertEqual(self.comment.email, "ali@example.com")
        self.assertEqual(self.comment.message, "عالی بود")
        self.assertTrue(self.comment.date)
