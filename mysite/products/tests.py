from django.test import TestCase
from .models import Product, generate_code, generate_price
from django.urls import reverse

class ProductModelTests(TestCase):
    def test_generate_code_returns_alphanum(self):
        desired_length = 4
        product = Product(name='P1')

        self.assertIs(len(generate_code()), desired_length)
        self.assertIs(generate_code().isalnum(), True)


class ProductsIndexViewTests(TestCase):
    def test_no_products(self):
        url = reverse('products:index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No products found.')
        self.assertQuerysetEqual(response.context['products'], [])

    def test_one_product(self):
        product = Product.objects.create(code='AAAA', name='P1')
        url = reverse('products:index')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products'], ['<Product: [AAAA] P1>'])

    def test_many_product(self):
        product1 = Product.objects.create(code='AAAA', name='P1')
        product2 = Product.objects.create(code='BBBB', name='P2')
        url = reverse('products:index')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['products']), ['<Product: [AAAA] P1>', '<Product: [BBBB] P2>'])


class ProductsDetailViewTests(TestCase):
    def valid_product_id(self):
        product = Product.objects.create(name='P', code='AAAA')
        url = reverse('products:detail', args=(product.id, ))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)
        self.assertContains(response, product.code)
        self.assertContains(response, product.desc)
        self.assertContains(response, product.price)

    def invalid_product_id(self):
        url = reverse('products:detail', args=(100, ))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)