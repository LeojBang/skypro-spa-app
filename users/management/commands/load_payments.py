# users/management/commands/load_payments.py
from django.core.management.base import BaseCommand
from users.models import Payment, User
from lms.models import Course, Lesson
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Load test payments data into database'

    def handle(self, *args, **options):
        # Получаем или создаем тестовые данные
        user = User.objects.get_or_create(
            email='testuser@example.com',
            defaults={
                'first_name': 'Test',
                'last_name': 'User',
                'phone': '+1234567890',
                'city': 'Test City'
            }
        )[0]

        course = Course.objects.get_or_create(
            name='Test Course',
            defaults={
                'description': 'Test Course Description'
            }
        )[0]

        lesson = Lesson.objects.get_or_create(
            course=course,
            name='Test Lesson',
            defaults={
                'description': 'Test Lesson Description'
            }
        )[0]

        # Создаем платежи
        payment_methods = ['Cash', 'Non_cash']
        payments = []

        for i in range(1, 11):
            payment_date = datetime.now() - timedelta(days=random.randint(1, 30))
            payment = Payment(
                user=user,
                payment_date=payment_date,
                price=random.randint(1000, 10000),
                payment_method=random.choice(payment_methods),
                payment_course=course if i % 2 == 0 else None,
                payment_lesson=lesson if i % 2 != 0 else None
            )
            payments.append(payment)

        Payment.objects.bulk_create(payments)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(payments)} payments'))