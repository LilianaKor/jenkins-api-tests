Agent Coding Manifest
Object Model and Design

Constructors (__init__) should contain only attribute assignments and simple initialization.

Classes should be conceptually final — minimize inheritance; prefer composition and protocols over hierarchies.

Setters should be avoided to keep objects as immutable as possible.

Use immutability whenever possible (@dataclass(frozen=True) or explicit absence of mutations).

Every entity should follow a DDD approach (explicit Value Objects, Entities, Aggregates).

Elegant Objects principles should be followed (clean objects, encapsulation, no data leakage).

Class names must not end with the suffix -er.

Each class must have only one primary constructor (__init__).

A class may contain no more than four attributes.

Every class must contain at least one attribute.

Utility classes are forbidden; any “utility” functions should exist as separate modules or objects.

Public constants should reside in modules, not inside classes.

Interfaces and Methods

Use Protocols (typing.Protocol) for contracts instead of traditional inheritance.

Public class methods should adhere to the contracts declared in interface protocols.

Methods should strictly follow CQRS principles:

Verbs (modify the state of another object)

Nouns (return a computed value)

Methods should not return None, unless explicitly part of a protocol.

Methods should avoid checking incoming arguments; passing None as an argument is unacceptable.

Exceptions must include context and a precise description of the problem.

Python-Specific Restrictions

Do not use @staticmethod or @classmethod if it turns the class into a “function container”; prefer pure module-level functions.

Avoid global variables and singletons; instead, explicitly pass dependencies.

Do not use introspection (e.g., isinstance(), type(), accessing __dict__).

Do not use reflection (e.g., getattr, dynamic method creation, monkey patching).

Do not use mutable default arguments in functions ([], {}, etc.).

Use immutable alternatives for collections where needed (tuple, Mapping, frozenset).

Modules should be small, follow SRP, and contain closely related entities.

Each method should be short and perform a single task.

Clean Code Practices

Use dataclasses only if they fit the Value Object pattern.

Packages should contain logically related bounded contexts.

Method and class names should be expressive and precise; prefer a longer descriptive name over an unclear one.

Code should not rely on “magic,” hidden dependencies, or dynamic tricks.

All I/O must be separated from the domain model (pure domain model + separate adapters).

Specific Prohibitions

Static methods acting as utility functions are forbidden.

Inheritance for implementation purposes is forbidden.

Public mutable attributes are forbidden (use properties and private attributes if necessary).

Methods that return different types depending on input are forbidden.

null (in Python — None) must not be used where an object is expected.
