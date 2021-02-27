from django.test import TestCase
from .models import Order
from django.urls import reverse
from django.utils import timezone

class OrderModelTests(TestCase):
    # case 1: gen_code returns alphanum
    def test_order_generate_code_is_alphanum(self):
        desired_length = 8
        order = Order()
        self.assertIs(len(order.code), desired_length)
        self.assertIs(str(order.code).isalnum(), True)


class OrdersIndexViewTests(TestCase):
    # case 1: no orders
    def test_no_orders(self):
        url = reverse('orders:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No orders found.')
        self.assertQuerysetEqual(response.context['orders'], [])
    
    # case 2: one order
    def test_one_order(self):
        order = Order.objects.create(code='ABCDEFGH')

        url = reverse('orders:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['orders'], ['<Order: [ABCDEFGH]>'])

    # case 3: many orders
    def test_many_orders(self):
        order1 = Order.objects.create(code='ABCDEFGH')
        order2 = Order.objects.create(code='AAAAAAA1')

        url = reverse('orders:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context['orders']),
            ['<Order: [ABCDEFGH]>', '<Order: [AAAAAAA1]>'])


class OrdersDetailViewTests(TestCase):
    # case 1: valid order id
    def test_valid_order_id(self):
        order = Order.objects.create()

        url = reverse('orders:detail', args=(order.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, order.code)
        # self.assertContains(response, order.date)
        self.assertContains(response, order.customer)

    def test_invalid_order_id(self):
        url = reverse('orders:detail', args=(999,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)