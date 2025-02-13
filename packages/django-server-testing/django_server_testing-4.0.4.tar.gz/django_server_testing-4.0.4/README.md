# Documentation for django_server_testing

Simple http server tester using Django


## Installation

Run `pip install django-server-testing`


## Usage Example

```python
from unittest import TestCase
import unittest
from urllib.request import urlopen

from django_server_testing import TestServer, Response, HttpHeaderStorage


class UrllibTestCase(TestCase):
   @classmethod
   def setUpClass(cls):
       cls.server = TestServer()
       cls.server.start()

   @classmethod
   def tearDownClass(cls):
       cls.server.stop()

   def setUp(self):
       self.server.reset()

   def test_get(self):
       self.server.add_response(
           Response(
               data=b"hello",
               headers={"foo": "bar"},
           )
       )
       self.server.add_response(Response(data=b"zzz"))
       url = self.server.get_url()
       info = urlopen(url)
       self.assertEqual(b"hello", info.read())
       self.assertEqual("bar", info.headers["foo"])
       info = urlopen(url)
       self.assertEqual(b"zzz", info.read())
       self.assertTrue("bar" not in info.headers)


   unittest.main()
```
