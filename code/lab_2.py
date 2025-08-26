import random
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class PackagingOrder:
    """
    Represents a packaging order containing apples.
    """

    # Constraints as class-level constants
    MAX_NB_APPLES: ClassVar[int] = 1000
    MAX_WEIGHT: ClassVar[float] = 100.0
    APPLE_WEIGHT_MIN: ClassVar[float] = 0.2
    APPLE_WEIGHT_MAX: ClassVar[float] = 0.5

    # State as instance-level variable attributes
    nb_apples_processed: int = 0
    total_weight: float = 0.0

    def add_apples(self, nb_apples: int) -> int:
        """
        Try to add apples to the order without exceeding constraints.

        Args:
            nb_apples: Number of apples to try to add.

        Returns:
            int: Number of apples successfully added.
        """
        
        added = 0
        for _ in range(nb_apples):

            # Apply max apples constraint
            if self.nb_apples_processed >= self.MAX_NB_APPLES:
                break
            
            # Generage candidate apple weight
            current_apple_weight = random.uniform(
                self.APPLE_WEIGHT_MIN, self.APPLE_WEIGHT_MAX
            )

            # Apply max total weight constraint
            if self.total_weight + current_apple_weight > self.MAX_WEIGHT:
                break

            # Update state
            self.total_weight += current_apple_weight
            self.nb_apples_processed += 1
            added += 1

        return added

    def __str__(self):
        return (f"Apples: {self.nb_apples_processed}, "
                f"Weight: {self.total_weight:.2f} kg")


# Runner code
order = PackagingOrder()
n = order.add_apples(int(10E4))
print(f"Added {n} apples → {order}")
