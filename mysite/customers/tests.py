from django.test import TestCase
from django.urls import reverse
from .models import Customer


class CustomersIndexTests(TestCase):
    # case 1: no customers
    def test_no_customers(self):
        response = self.client.get(reverse('customers:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['customers'], [])
        self.assertContains(response, 'No customers found.')

    # case 2: one customer
    def test_one_customer(self):
        customer = Customer.objects.create(name='Test-Customer')
        
        response = self.client.get(reverse('customers:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['customers'], ['<Customer: Test-Customer>'])
    
    # case 3: many customers
    def test_many_customers(self):
        customer1 = Customer.objects.create(name='Test-Customer-1', email='c1@mail.com')
        customer2 = Customer.objects.create(name='Test-Customer-2', email='c2@mail.com')

        response = self.client.get(reverse('customers:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            list(response.context['customers']),
            ['<Customer: Test-Customer-1>', '<Customer: Test-Customer-2>']
        )


class CustomersDetailViewTests(TestCase):
    # case 1: invalid customer id in url
    def test_invalid_customer_id(self):
        url = reverse('customers:customer', args=(100, )) # 100 as invalid id
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # case 2: valid customer id in url
    def test_valid_customer_id(self):
        customer = Customer.objects.create(name='Test-Customer', email='test@mail.com', password='test')
        url = reverse('customers:customer', args=(customer.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test-Customer')
        self.assertContains(response, 'test@mail.com')
        self.assertContains(response, 'test')