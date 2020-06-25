import string, random
from .models import Orden


class OrderIdGenerator:

    id_generator_size = 6

    id_generator_attempts = 0

    @classmethod
    def generate_order_id(cls, size=6, chars=string.ascii_uppercase + string.digits):
        order_id = ''.join(random.choice(chars) for _ in range(size))
        try:
            existing = Orden.objects.get(order_id=order_id)
        except Orden.DoesNotExist:
            return order_id
        cls.id_generator_attempts += 1
        if cls.id_generator_attempts > 5:
            cls.id_generator_size += 1
        return cls.generate_order_id(cls.id_generator_size)
