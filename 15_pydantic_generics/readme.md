# [Modern Python - Lesson 15: Pydantic & Generics](https://colab.research.google.com/drive/15nZDVUsTrXcIU3pyqaWtg0kPXWbmiJrh?usp=sharing)

## Table of Contents
1. [Introduction to Pydantic](#introduction-to-pydantic)
2. [Pydantic Installation](#pydantic-installation)
3. [Basic Pydantic Models](#basic-pydantic-models)
4. [Field Validation](#field-validation)
5. [Nested Models](#nested-models)
6. [JSON Serialization](#json-serialization)
7. [Settings Management](#settings-management)
8. [Custom Validators](#custom-validators)
9. [Introduction to Generics](#introduction-to-generics)
10. [What Are Generics?](#what-are-generics)
11. [Why Are Generics Needed?](#why-are-generics-needed)
12. [How Generics Work in Python 3.12](#how-generics-work-in-python-312)
13. [New Features in Python 3.12](#new-features-in-python-312)
14. [Basic Generic Functions](#basic-generic-functions)
15. [Generic Classes](#generic-classes)
16. [TypeVar and Bounds](#typevar-and-bounds)
17. [Generic Collections](#generic-collections)
18. [Overloading with @overload](#overloading-with-overload)
19. [Real-World Examples](#real-world-examples)
20. [Best Practices](#best-practices)
21. [Key Concepts Summary](#key-concepts-summary)
22. [Useful Links](#useful-links)

---

## Introduction to Pydantic

Pydantic is a powerful Python library for **data validation and settings management** using Python type hints. It ensures your data is always in the correct format, making it perfect for APIs, configuration management, and data parsing.

### Pydantic Overview

```mermaid
graph TD
    A["Pydantic"] --> B["Data Validation"]
    A --> C["Settings Management"]
    A --> D["Type Safety"]
    A --> E["Serialization"]
    
    B --> B1["Field validation"]
    B --> B2["Custom validators"]
    B --> B3["Error handling"]
    
    C --> C1["Environment variables"]
    C --> C2["Configuration files"]
    C --> C3["Default values"]
    
    D --> D1["Type hints required"]
    D --> D2["Runtime validation"]
    D --> D3["IDE support"]
    
    E --> E1["JSON serialization"]
    E --> E2["Model conversion"]
    E --> E3["API responses"]
```

**Diagram Explanation**: This diagram shows the core features of Pydantic, including data validation, settings management, type safety, and serialization capabilities.

### Key Benefits

- **Type Safety**: Ensures data matches expected types
- **Automatic Validation**: Validates data based on type hints
- **JSON Serialization**: Easy conversion to/from JSON
- **Settings Management**: Perfect for configuration files
- **Error Handling**: Clear validation error messages
- **IDE Support**: Better autocomplete and error detection

### Perfect Use Cases

✅ **API request/response validation**  
✅ **Configuration management**  
✅ **Data parsing & serialization**  
✅ **Environment variable handling**  
✅ **Database model validation**

## Pydantic Installation

Installing Pydantic is straightforward and includes several optional features.

### Installation Commands

```bash
# Basic installation
pip install pydantic

# With settings management
pip install pydantic pydantic_settings

# With email validation
pip install pydantic[email]

# All features
pip install pydantic pydantic_settings pydantic[email]
```

### Installation Verification

```python
from pydantic import BaseModel
from pydantic_settings import BaseSettings

# Test basic functionality
class TestModel(BaseModel):
    name: str
    age: int

test = TestModel(name="Alice", age=25)
print(test)  # Output: TestModel(name='Alice', age=25)
```

## Basic Pydantic Models

Creating basic Pydantic models is simple and leverages Python's type hinting system.

### Model Creation

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool = True  # Default value

# Usage
user = User(name="Alice", age=25)
print(user.name)  # Output: "Alice"
print(user.age)   # Output: 25
print(user.is_active)  # Output: True (default)
```

### Automatic Validation

```python
# ✅ Valid data
user = User(name="Bob", age=30)
print(user)  # Output: User(name='Bob', age=30, is_active=True)

# ❌ Invalid data - will raise ValidationError
try:
    user = User(name="Charlie", age="twenty")  # age must be int
except ValidationError as e:
    print(f"Validation error: {e}")
```

### Model Structure

```mermaid
graph TD
    A["BaseModel"] --> B["User Class"]
    B --> C["name: str"]
    B --> D["age: int"]
    B --> E["is_active: bool = True"]
    
    C --> C1["Required field"]
    D --> D1["Required field"]
    E --> E1["Optional with default"]
    
    F["Validation"] --> G["Type checking"]
    F --> H["Required field checking"]
    F --> I["Default value assignment"]
```

**Diagram Explanation**: This diagram shows the structure of a basic Pydantic model, including field types, requirements, and validation flow.

## Field Validation

Pydantic provides powerful field validation capabilities using the `Field` function to add extra validation rules.

### Field Validation Overview

```mermaid
graph TD
    A["Field Validation"] --> B["Type Validation"]
    A --> C["Range Validation"]
    A --> D["Length Validation"]
    A --> E["Custom Validation"]
    
    B --> B1["int, str, float"]
    B --> B2["Optional types"]
    B --> B3["Union types"]
    
    C --> C1["gt (greater than)"]
    C --> C2["ge (greater equal)"]
    C --> C3["lt (less than)"]
    C --> C4["le (less equal)"]
    
    D --> D1["min_length"]
    D --> D2["max_length"]
    D --> D3["regex patterns"]
    
    E --> E1["Custom validators"]
    E --> E2["Field validators"]
    E --> E3["Model validators"]
```

**Diagram Explanation**: This diagram shows the different types of field validation available in Pydantic, including type, range, length, and custom validation.

### Using Field for Validation Rules

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)  # Must be > 0
    category: str = Field(min_length=3, max_length=50)
    stock: int = Field(ge=0)  # Must be >= 0

# ✅ Valid product
product = Product(
    name="Laptop", 
    price=999.99, 
    category="Electronics",
    stock=10
)
print(product)  # Output: Product(name='Laptop', price=999.99, category='Electronics', stock=10)

# ❌ Invalid product (price <= 0)
try:
    product = Product(name="Phone", price=0, category="Gadgets", stock=5)
except ValidationError as e:
    print(f"Validation error: {e}")
```

### Field Validation Options

| Validation | Description | Example |
|------------|-------------|---------|
| `gt` | Greater than | `Field(gt=0)` |
| `ge` | Greater than or equal | `Field(ge=0)` |
| `lt` | Less than | `Field(lt=100)` |
| `le` | Less than or equal | `Field(le=100)` |
| `min_length` | Minimum string length | `Field(min_length=3)` |
| `max_length` | Maximum string length | `Field(max_length=50)` |
| `regex` | Regular expression pattern | `Field(regex=r'^[A-Z]')` |

### Advanced Field Validation

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20, regex=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    age: int = Field(ge=13, le=120)
    bio: Optional[str] = Field(None, max_length=500)
    website: Optional[str] = Field(None, regex=r'^https?://')

# Usage
profile = UserProfile(
    username="alice123",
    email="alice@example.com",
    age=25,
    bio="Software developer",
    website="https://alice.dev"
)
print(profile)
```

## Nested Models

Pydantic supports nested models, allowing you to create complex data structures with validation at multiple levels.

### Nested Model Structure

```mermaid
graph TD
    A["UserProfile"] --> B["name: str"]
    A --> C["address: Address"]
    A --> D["contacts: List[Contact]"]
    
    C --> C1["city: str"]
    C --> C2["country: str"]
    C --> C3["postal_code: str"]
    
    D --> D1["Contact 1"]
    D --> D2["Contact 2"]
    D --> D3["Contact N"]
    
    D1 --> E1["type: str"]
    D1 --> E2["value: str"]
```

**Diagram Explanation**: This diagram shows how nested models work in Pydantic, with a UserProfile containing an Address and a list of Contacts.

### Basic Nested Models

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    country: str
    postal_code: str

class UserProfile(BaseModel):
    name: str
    address: Address  # Nested model
    age: int

# Usage with dictionary input
profile = UserProfile(
    name="Alice",
    address={"city": "New York", "country": "USA", "postal_code": "10001"},
    age=25
)
print(profile.address.city)  # Output: "New York"
print(profile.address.country)  # Output: "USA"
```

### Complex Nested Models

```python
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Contact(BaseModel):
    type: str  # "email", "phone", "social"
    value: str
    is_primary: bool = False

class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str
    is_primary: bool = False

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: int
    address: Address
    contacts: List[Contact] = []
    emergency_contact: Optional[Contact] = None

# Usage
profile = UserProfile(
    name="Alice Johnson",
    email="alice@example.com",
    age=25,
    address={
        "street": "123 Main St",
        "city": "New York",
        "country": "USA",
        "postal_code": "10001",
        "is_primary": True
    },
    contacts=[
        {"type": "phone", "value": "+1-555-0123", "is_primary": True},
        {"type": "social", "value": "@alice_j", "is_primary": False}
    ],
    emergency_contact={"type": "phone", "value": "+1-555-9999", "is_primary": False}
)

print(f"Primary contact: {profile.contacts[0].value}")
print(f"Address: {profile.address.street}, {profile.address.city}")
```

### Nested Model Validation

```python
# All nested models are automatically validated
try:
    profile = UserProfile(
        name="Bob",
        email="invalid-email",  # ❌ Invalid email format
        age=25,
        address={"city": "NYC", "country": "USA", "postal_code": "10001"},
        contacts=[]
    )
except ValidationError as e:
    print(f"Validation error: {e}")
```

## JSON Serialization

Pydantic provides excellent JSON serialization capabilities, making it easy to convert models to and from JSON format.

### Serialization Overview

```mermaid
graph TD
    A["Pydantic Model"] --> B["JSON Serialization"]
    B --> C["model_dump_json()"]
    B --> D["model_dump()"]
    
    A --> E["JSON Deserialization"]
    E --> F["model_validate_json()"]
    E --> G["model_validate()"]
    
    C --> H["JSON string"]
    D --> I["Python dict"]
    F --> J["From JSON string"]
    G --> K["From Python dict"]
```

**Diagram Explanation**: This diagram shows the bidirectional serialization capabilities of Pydantic models.

### Basic JSON Operations

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool = True

# Create a user
user = User(name="Bob", age=30)

# Model → JSON string
user_json = user.model_dump_json()
print(user_json)
# Output: '{"name":"Bob","age":30,"is_active":true}'

# Model → Python dict
user_dict = user.model_dump()
print(user_dict)
# Output: {'name': 'Bob', 'age': 30, 'is_active': True}

# JSON string → Model
new_user = User.model_validate_json('{"name":"Charlie","age":40}')
print(new_user.name)  # Output: "Charlie"
print(type(new_user))  # Output: <class '__main__.User'>

# Python dict → Model
user_from_dict = User.model_validate({"name": "David", "age": 35})
print(user_from_dict)  # Output: User(name='David', age=35, is_active=True)
```

### Advanced Serialization Options

```python
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    password: str = Field(..., exclude=True)  # Exclude from serialization

# Create user
user = User(name="Alice", age=25, email="alice@example.com", password="secret123")

# Serialize with exclusions
user_dict = user.model_dump(exclude={"password"})
print(user_dict)  # Output: {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'}

# Serialize only specific fields
user_dict = user.model_dump(include={"name", "age"})
print(user_dict)  # Output: {'name': 'Alice', 'age': 25}

# Serialize with custom field names
user_dict = user.model_dump(by_alias=True)
print(user_dict)
```

### Nested Model Serialization

```python
from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address
    hobbies: List[str] = []

# Create user with nested data
user = User(
    name="Alice",
    age=25,
    address={"city": "New York", "country": "USA"},
    hobbies=["reading", "coding", "hiking"]
)

# Serialize to JSON
user_json = user.model_dump_json(indent=2)
print(user_json)
# Output: Pretty-printed JSON with nested structure

# Deserialize from JSON
json_data = '''
{
    "name": "Bob",
    "age": 30,
    "address": {
        "city": "London",
        "country": "UK"
    },
    "hobbies": ["music", "travel"]
}
'''
new_user = User.model_validate_json(json_data)
print(new_user.address.city)  # Output: "London"
```

## Settings Management

Pydantic is excellent for configuration management, especially when working with environment variables and configuration files.

### Settings Management Overview

```mermaid
graph TD
    A["Settings Management"] --> B["Environment Variables"]
    A --> C["Configuration Files"]
    A --> D["Default Values"]
    A --> E["Validation"]
    
    B --> B1[".env files"]
    B --> B2["System environment"]
    B --> B3["Docker secrets"]
    
    C --> C1["JSON configs"]
    C --> C2["YAML configs"]
    C --> C3["TOML configs"]
    
    D --> D1["Fallback values"]
    D --> D2["Optional settings"]
    D --> D3["Development defaults"]
    
    E --> E1["Type validation"]
    E --> E2["Required fields"]
    E --> E3["Custom validators"]
```

**Diagram Explanation**: This diagram shows the different aspects of settings management with Pydantic, including environment variables, configuration files, defaults, and validation.

### Basic Settings Management

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = "default-key"  # Default value
    debug: bool = False
    database_url: str = "sqlite:///app.db"
    max_connections: int = 100

    class Config:
        env_file = ".env"  # Load from .env file

# Usage
settings = Settings()
print(settings.api_key)  # Output: "default-key" (or from .env)
print(settings.debug)    # Output: False (or from .env)
```

### Environment File Example

```bash
# .env file
API_KEY=my-secret-key-123
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost/db
MAX_CONNECTIONS=200
```

### Advanced Settings Management

```python
from pydantic_settings import BaseSettings
from pydantic import Field, validator
from typing import Optional, List

class DatabaseSettings(BaseSettings):
    host: str = "localhost"
    port: int = Field(default=5432, ge=1, le=65535)
    username: str
    password: str
    database: str
    ssl_mode: bool = False

class APISettings(BaseSettings):
    title: str = "My API"
    version: str = "1.0.0"
    description: str = "A sample API"
    allowed_hosts: List[str] = ["localhost", "127.0.0.1"]
    cors_origins: List[str] = ["http://localhost:3000"]

class Settings(BaseSettings):
    # Nested settings
    database: DatabaseSettings = DatabaseSettings()
    api: APISettings = APISettings()
    
    # Top-level settings
    environment: str = Field(default="development", regex=r'^(development|staging|production)$')
    log_level: str = Field(default="INFO", regex=r'^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$')
    secret_key: str = Field(..., min_length=32)  # Required, minimum 32 characters
    
    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"  # For nested settings like DATABASE__HOST

# Usage
settings = Settings()
print(f"Database: {settings.database.host}:{settings.database.port}")
print(f"API: {settings.api.title} v{settings.api.version}")
print(f"Environment: {settings.environment}")
```

### Environment Variable Mapping

```python
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Environment variable names can be customized
    api_key: str = Field(alias="MY_API_KEY")
    debug_mode: bool = Field(alias="DEBUG", default=False)
    database_url: str = Field(alias="DATABASE_URL")
    
    class Config:
        env_file = ".env"
        case_sensitive = False  # Case insensitive environment variables

# Environment variables:
# MY_API_KEY=secret123
# DEBUG=true
# DATABASE_URL=postgresql://...
```

## Custom Validators

Pydantic allows you to define custom validation logic using validators for more complex validation rules.

### Custom Validators Overview

```mermaid
graph TD
    A["Custom Validators"] --> B["Field Validators"]
    A --> C["Model Validators"]
    A --> D["Root Validators"]
    
    B --> B1["@field_validator"]
    B --> B2["Single field validation"]
    B --> B3["Transform values"]
    
    C --> C1["@model_validator"]
    C --> C2["Multiple field validation"]
    C --> C3["Cross-field validation"]
    
    D --> D1["@root_validator"]
    D --> D2["Entire model validation"]
    D --> D3["Complex business rules"]
```

**Diagram Explanation**: This diagram shows the different types of custom validators available in Pydantic, from field-level to model-level validation.

### Field Validators

```python
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    username: str

    @field_validator("name")
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty!")
        return value.strip().title()  # Transform to title case

    @field_validator("age")
    def age_must_be_reasonable(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        if value > 150:
            raise ValueError("Age cannot be more than 150!")
        return value

    @field_validator("username")
    def username_must_be_valid(cls, value):
        if not value.isalnum():
            raise ValueError("Username must contain only letters and numbers!")
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long!")
        return value.lower()

# Valid user
user = User(
    name="  alice smith  ",  # Will be transformed to "Alice Smith"
    email="alice@example.com",
    age=25,
    username="Alice123"  # Will be transformed to "alice123"
)
print(user)  # Output: User(name='Alice Smith', email='alice@example.com', age=25, username='alice123')

# Invalid user (empty name)
try:
    user = User(name=" ", email="alice@example.com", age=25, username="alice123")
except ValueError as e:
    print(f"Validation error: {e}")
```

### Model Validators

```python
from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime, date

class Event(BaseModel):
    name: str
    start_date: date
    end_date: date
    max_attendees: int
    current_attendees: int = 0

    @model_validator(mode='after')
    def validate_dates_and_capacity(self):
        # Validate date range
        if self.start_date >= self.end_date:
            raise ValueError("End date must be after start date")
        
        # Validate capacity
        if self.current_attendees > self.max_attendees:
            raise ValueError("Current attendees cannot exceed maximum capacity")
        
        # Validate capacity is reasonable
        if self.max_attendees <= 0:
            raise ValueError("Maximum attendees must be positive")
        
        return self

# Valid event
event = Event(
    name="Python Conference",
    start_date=date(2024, 6, 1),
    end_date=date(2024, 6, 3),
    max_attendees=500,
    current_attendees=150
)
print(event)

# Invalid event (end date before start date)
try:
    event = Event(
        name="Invalid Event",
        start_date=date(2024, 6, 3),
        end_date=date(2024, 6, 1),  # End before start
        max_attendees=100,
        current_attendees=50
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

### Advanced Custom Validators

```python
from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional
import re

class PasswordPolicy(BaseModel):
    min_length: int = 8
    require_uppercase: bool = True
    require_lowercase: bool = True
    require_numbers: bool = True
    require_special: bool = True

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str
    age: int
    interests: List[str] = []

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return value.lower()

    @field_validator("password")
    def validate_password(cls, value, info):
        # Get password policy from context if available
        policy = PasswordPolicy()  # In real app, this might come from settings
        
        if len(value) < policy.min_length:
            raise ValueError(f"Password must be at least {policy.min_length} characters")
        
        if policy.require_uppercase and not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter")
        
        if policy.require_lowercase and not re.search(r'[a-z]', value):
            raise ValueError("Password must contain at least one lowercase letter")
        
        if policy.require_numbers and not re.search(r'\d', value):
            raise ValueError("Password must contain at least one number")
        
        if policy.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError("Password must contain at least one special character")
        
        return value

    @model_validator(mode='after')
    def validate_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

    @field_validator("interests")
    def validate_interests(cls, value):
        if len(value) > 10:
            raise ValueError("Cannot have more than 10 interests")
        return [interest.strip().title() for interest in value if interest.strip()]

# Valid registration
user = UserRegistration(
    username="alice123",
    email="alice@example.com",
    password="SecurePass123!",
    confirm_password="SecurePass123!",
    age=25,
    interests=["python", "machine learning", "web development"]
)
print(user)

# Invalid registration (passwords don't match)
try:
    user = UserRegistration(
        username="bob456",
        email="bob@example.com",
        password="SecurePass123!",
        confirm_password="DifferentPass123!",
        age=30,
        interests=[]
    )
except ValueError as e:
    print(f"Validation error: {e}")
```

## Introduction to Generics

Generics in Python 3.12 represent a significant advancement in the type hinting system, making it easier to write reusable, type-safe code. This section covers everything you need to know about generics in Python 3.12.

### Generics Overview

```mermaid
graph TD
    A["Generics in Python 3.12"] --> B["Type Safety"]
    A --> C["Code Reusability"]
    A --> D["Better Syntax"]
    A --> E["Enhanced Features"]
    
    B --> B1["Static type checking"]
    B --> B2["Runtime validation"]
    B --> B3["IDE support"]
    
    C --> C1["Generic functions"]
    C --> C2["Generic classes"]
    C --> C3["Generic collections"]
    
    D --> D1["Inline syntax"]
    D --> D2["Type parameter lists"]
    D --> D3["Simplified TypeVar"]
    
    E --> E1["Better error messages"]
    E --> E2["Improved bounds"]
    E --> E3["Enhanced overloading"]
```

**Diagram Explanation**: This diagram shows the key benefits and features of generics in Python 3.12, including type safety, code reusability, improved syntax, and enhanced features.

### Key Improvements in Python 3.12

| Feature | Python 3.11 and Earlier | Python 3.12 |
|---------|-------------------------|--------------|
| **Syntax** | `from typing import TypeVar` | `def func[T](): ...` |
| **Type Parameters** | `T = TypeVar('T')` | `class Stack[T]: ...` |
| **Collections** | `List[T]`, `Dict[K, V]` | `list[T]`, `dict[K, V]` |
| **Error Messages** | Complex, hard to read | Clear, actionable |
| **Bounds** | `TypeVar('T', bound=int)` | `T = TypeVar('T', bound=int)` |

## What Are Generics?

Generics enable you to parameterize types, meaning you can create a blueprint for a class or function that works with any type (or a constrained set of types) specified by the user of that code.

### Core Concept

```mermaid
graph TD
    A["Generic Concept"] --> B["Type Parameterization"]
    A --> C["Code Reusability"]
    A --> D["Type Safety"]
    
    B --> B1["T, K, V parameters"]
    B --> B2["Multiple type parameters"]
    B --> B3["Type constraints"]
    
    C --> C1["One implementation"]
    C --> C2["Multiple types"]
    C --> C3["DRY principle"]
    
    D --> D1["Compile-time checking"]
    D --> D2["Runtime validation"]
    D --> D3["IDE support"]
```

**Diagram Explanation**: This diagram illustrates the core concept of generics, showing how type parameterization enables code reusability while maintaining type safety.

### Example: Without Generics

```python
# ❌ Without generics - need separate functions for each type
def process_int_list(items):
    return [item * 2 for item in items]

def process_str_list(items):
    return [item.upper() for item in items]

def process_float_list(items):
    return [item * 1.5 for item in items]

# Usage
int_list = process_int_list([1, 2, 3])  # [2, 4, 6]
str_list = process_str_list(["a", "b"])  # ["A", "B"]
float_list = process_float_list([1.0, 2.0])  # [1.5, 3.0]
```

### Example: With Generics

```python
# ✅ With generics - one function for all types
def process_list[T](items: list[T]) -> list[T]:
    if not items:
        return items
    
    # Type-specific processing based on the first item
    first_item = items[0]
    if isinstance(first_item, int):
        return [item * 2 for item in items]
    elif isinstance(first_item, str):
        return [item.upper() for item in items]
    elif isinstance(first_item, float):
        return [item * 1.5 for item in items]
    else:
        return items

# Usage - same function, different types
int_list = process_list([1, 2, 3])  # [2, 4, 6]
str_list = process_list(["a", "b"])  # ["A", "B"]
float_list = process_list([1.0, 2.0])  # [1.5, 3.0]
```

## Why Are Generics Needed?

Understanding the problems generics solve helps appreciate their value in modern Python development.

### Problems Generics Solve

```mermaid
graph TD
    A["Problems Generics Solve"] --> B["Code Duplication"]
    A --> C["Type Safety"]
    A --> D["Maintainability"]
    A --> E["Performance"]
    
    B --> B1["DRY principle"]
    B --> B2["Single implementation"]
    B --> B3["Reduced complexity"]
    
    C --> C1["Static checking"]
    C --> C2["Runtime validation"]
    C --> C3["IDE support"]
    
    D --> D1["Easier debugging"]
    D --> D2["Better documentation"]
    D --> D3["Consistent behavior"]
    
    E --> E1["No runtime overhead"]
    E --> E2["Optimized execution"]
    E --> E3["Memory efficiency"]
```

**Diagram Explanation**: This diagram shows the key problems that generics solve, including code duplication, type safety, maintainability, and performance.

### 1. Code Reusability

**Without Generics:**
```python
# Need separate implementations for each type
class IntStack:
    def __init__(self):
        self.items = []
    
    def push(self, item: int):
        self.items.append(item)
    
    def pop(self) -> int:
        return self.items.pop()

class StrStack:
    def __init__(self):
        self.items = []
    
    def push(self, item: str):
        self.items.append(item)
    
    def pop(self) -> str:
        return self.items.pop()

# Duplicate code for each type!
```

**With Generics:**
```python
# Single implementation for all types
class Stack[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()

# Usage with different types
int_stack = Stack[int]()
str_stack = Stack[str]()
float_stack = Stack[float]()
```

### 2. Type Safety

```python
from typing import TypeVar

# Define a type variable with constraints
T = TypeVar('T', bound=int | str)  # Only int or str allowed

def process_value(value: T) -> T:
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    else:
        raise TypeError("Unsupported type")

# ✅ Valid usage
result1 = process_value(42)  # Returns 84 (int)
result2 = process_value("hello")  # Returns "HELLO" (str)

# ❌ Invalid usage - type checker will catch this
# result3 = process_value(3.14)  # Error: float not allowed
```

### 3. Abstraction

```python
# Generic data structure that works with any type
class Container[T]:
    def __init__(self, value: T):
        self.value = value
    
    def get(self) -> T:
        return self.value
    
    def set(self, value: T) -> None:
        self.value = value
    
    def transform[U](self, func: callable[[T], U]) -> Container[U]:
        return Container(func(self.value))

# Usage with different types
int_container = Container(42)
str_container = Container("hello")
list_container = Container([1, 2, 3])

# Transform to different types
str_from_int = int_container.transform(str)  # Container[str] with "42"
length_from_str = str_container.transform(len)  # Container[int] with 5
```

### 4. Interoperability

```python
# Generic API response that works with any data type
class APIResponse[T]:
    def __init__(self, data: T, status_code: int, message: str = "Success"):
        self.data = data
        self.status_code = status_code
        self.message = message
    
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300
    
    def get_data(self) -> T:
        if self.is_success():
            return self.data
        else:
            raise ValueError(f"API Error: {self.message}")

# Usage with different data types
user_response = APIResponse[dict](
    data={"id": 1, "name": "Alice"}, 
    status_code=200
)

list_response = APIResponse[list](
    data=[1, 2, 3, 4, 5], 
    status_code=200
)

string_response = APIResponse[str](
    data="Hello World", 
    status_code=200
)
```

## How Generics Work in Python 3.12

Understanding the mechanics of generics helps you use them effectively in your code.

### Generic Function Syntax

```python
# Python 3.12 syntax
def swap[T](a: T, b: T) -> tuple[T, T]:
    return b, a

# Usage
x, y = swap(10, 20)    # (int, int)
a, b = swap("A", "B")  # (str, str)
```

### Generic Class Syntax

```python
# Python 3.12 syntax
class Stack[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()
    
    def peek(self) -> T:
        return self.items[-1]

# Usage
int_stack = Stack[int]()
int_stack.push(42)
value = int_stack.pop()  # Type: int
```

### Multiple Type Parameters

```python
# Multiple type parameters
def get_value[K, V](d: dict[K, V], key: K) -> V:
    return d[key]

# Usage
person = {"name": "Alice", "age": 30}
name = get_value(person, "name")  # Returns "Alice" (str)
age = get_value(person, "age")    # Returns 30 (int)
```

### Type Parameter Bounds

```python
from typing import TypeVar

# Bounded type parameter
Numeric = TypeVar('Numeric', bound=int | float)

def add_numbers(a: Numeric, b: Numeric) -> Numeric:
    return a + b

# ✅ Valid usage
result1 = add_numbers(5, 10)      # int + int = int
result2 = add_numbers(3.14, 2.71) # float + float = float

# ❌ Invalid usage
# result3 = add_numbers("5", "10")  # Error: str not allowed
```

## New Features in Python 3.12

Python 3.12 introduces several improvements to generics, making them more powerful and easier to use.

### New Features Overview

```mermaid
graph TD
    A["Python 3.12 New Features"] --> B["Simpler Syntax"]
    A --> C["Type Parameter Lists"]
    A --> D["TypeVar Improvements"]
    A --> E["Better Error Messages"]
    
    B --> B1["No typing import needed"]
    B --> B2["Inline type parameters"]
    B --> B3["Cleaner code"]
    
    C --> C1["def func[T]()"]
    C --> C2["class Stack[T]"]
    C --> C3["Multiple parameters"]
    
    D --> D1["Easier bounds"]
    D --> D2["Better constraints"]
    D --> D3["Simplified syntax"]
    
    E --> E1["Clear error messages"]
    E --> E2["Actionable feedback"]
    E --> E3["Better debugging"]
```

**Diagram Explanation**: This diagram shows the new features introduced in Python 3.12 for generics, including simpler syntax, type parameter lists, TypeVar improvements, and better error messages.

### Feature Comparison

| Feature | Python 3.11 and Earlier | Python 3.12 |
|---------|-------------------------|--------------|
| **Function Syntax** | `from typing import TypeVar`<br>`T = TypeVar('T')`<br>`def func(x: T) -> T:` | `def func[T](x: T) -> T:` |
| **Class Syntax** | `class Stack(Generic[T]):` | `class Stack[T]:` |
| **Collections** | `List[T]`, `Dict[K, V]` | `list[T]`, `dict[K, V]` |
| **Bounds** | `TypeVar('T', bound=int)` | `T = TypeVar('T', bound=int)` |
| **Error Messages** | Complex, technical | Clear, actionable |

### Installation Note

**Important**: To use the new generic syntax in Python 3.12, you need to ensure you're running Python 3.12 or later. Google Colab may need to be updated to use Python 3.12.

```python
# Check Python version
import sys
print(sys.version)  # Should show 3.12.x

# For Google Colab, you may need to upgrade:
# !apt-get install python3.12
# !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
```

## Basic Generic Functions

Generic functions allow you to write functions that work with multiple types while maintaining type safety.

### Simple Generic Functions

```python
# Python 3.12 syntax
def identity[T](value: T) -> T:
    """Return the value unchanged."""
    return value

def first_item[T](items: list[T]) -> T:
    """Return the first item from a list."""
    if not items:
        raise ValueError("List is empty")
    return items[0]

def last_item[T](items: list[T]) -> T:
    """Return the last item from a list."""
    if not items:
        raise ValueError("List is empty")
    return items[-1]

# Usage
print(identity(42))  # Output: 42 (int)
print(identity("hello"))  # Output: "hello" (str)

numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

print(first_item(numbers))  # Output: 1 (int)
print(first_item(names))    # Output: "Alice" (str)
print(last_item(numbers))   # Output: 5 (int)
print(last_item(names))     # Output: "Charlie" (str)
```

### Multiple Type Parameters

```python
# Functions with multiple type parameters
def swap[T, U](a: T, b: U) -> tuple[U, T]:
    """Swap two values of potentially different types."""
    return b, a

def get_value[K, V](d: dict[K, V], key: K) -> V:
    """Get a value from a dictionary by key."""
    return d[key]

def create_pair[T, U](first: T, second: U) -> tuple[T, U]:
    """Create a pair from two values."""
    return first, second

# Usage
result = swap(42, "hello")  # Returns ("hello", 42)
print(result)  # Output: ("hello", 42)

person = {"name": "Alice", "age": 30}
name = get_value(person, "name")  # Returns "Alice" (str)
age = get_value(person, "age")    # Returns 30 (int)

pair = create_pair("key", 123)  # Returns ("key", 123)
print(pair)  # Output: ("key", 123)
```

### Generic Functions with Constraints

```python
from typing import TypeVar

# Type variable with bounds
Numeric = TypeVar('Numeric', bound=int | float)

def double[T: Numeric](value: T) -> T:
    """Double a numeric value."""
    return value * 2

def add[T: Numeric](a: T, b: T) -> T:
    """Add two numeric values."""
    return a + b

# Usage
print(double(5))      # Output: 10 (int)
print(double(3.14))   # Output: 6.28 (float)
print(add(10, 20))    # Output: 30 (int)
print(add(1.5, 2.5))  # Output: 4.0 (float)

# This would cause a type error:
# print(double("hello"))  # Error: str not allowed
```

## Generic Classes

Generic classes allow you to create classes that work with multiple types while maintaining type safety.

### Basic Generic Classes

```python
# Generic Stack class
class Stack[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self) -> T:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self) -> T:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

# Usage with different types
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())  # Output: 3

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # Output: "world"
```

### Generic Queue Class

```python
from collections import deque

class Queue[T]:
    def __init__(self):
        self.items: deque[T] = deque()
    
    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self) -> T:
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self) -> T:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

# Usage
queue = Queue[str]()
queue.enqueue("first")
queue.enqueue("second")
queue.enqueue("third")
print(queue.dequeue())  # Output: "first"
print(queue.front())    # Output: "second"
```

### Generic Container Class

```python
class Container[T]:
    def __init__(self, value: T):
        self.value = value
    
    def get(self) -> T:
        """Get the stored value."""
        return self.value
    
    def set(self, value: T) -> None:
        """Set a new value."""
        self.value = value
    
    def transform[U](self, func: callable[[T], U]) -> 'Container[U]':
        """Transform the value using a function."""
        return Container(func(self.value))
    
    def __repr__(self) -> str:
        return f"Container({self.value})"

# Usage
int_container = Container(42)
print(int_container.get())  # Output: 42

str_container = int_container.transform(str)
print(str_container.get())  # Output: "42"

length_container = str_container.transform(len)
print(length_container.get())  # Output: 2
```

### Generic API Response Class

```python
class APIResponse[T]:
    def __init__(self, data: T, status_code: int, message: str = "Success"):
        self.data = data
        self.status_code = status_code
        self.message = message
    
    def is_success(self) -> bool:
        """Check if the response indicates success."""
        return 200 <= self.status_code < 300
    
    def is_error(self) -> bool:
        """Check if the response indicates an error."""
        return not self.is_success()
    
    def get_data(self) -> T:
        """Get the response data."""
        if self.is_success():
            return self.data
        else:
            raise ValueError(f"API Error {self.status_code}: {self.message}")
    
    def __repr__(self) -> str:
        return f"APIResponse(data={self.data}, status_code={self.status_code}, message='{self.message}')"

# Usage with different data types
user_response = APIResponse[dict](
    data={"id": 1, "name": "Alice", "email": "alice@example.com"},
    status_code=200
)

list_response = APIResponse[list](
    data=[1, 2, 3, 4, 5],
    status_code=200
)

string_response = APIResponse[str](
    data="Operation completed successfully",
    status_code=200
)

error_response = APIResponse[None](
    data=None,
    status_code=404,
    message="Resource not found"
)

print(user_response.get_data())  # Output: {"id": 1, "name": "Alice", "email": "alice@example.com"}
print(list_response.get_data())  # Output: [1, 2, 3, 4, 5]
print(string_response.get_data())  # Output: "Operation completed successfully"

try:
    error_response.get_data()  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: API Error 404: Resource not found
```

## TypeVar and Bounds

TypeVar allows you to create type variables with constraints, providing more control over generic types.

### TypeVar Overview

```mermaid
graph TD
    A["TypeVar"] --> B["Unconstrained"]
    A --> C["Bounded"]
    A --> D["Constrained"]
    
    B --> B1["Any type allowed"]
    B --> B2["T = TypeVar('T')"]
    B --> B3["Maximum flexibility"]
    
    C --> C1["Bound to specific type"]
    C --> C2["T = TypeVar('T', bound=int)"]
    C --> C3["Inheritance constraint"]
    
    D --> D1["Specific types only"]
    D --> D2["T = TypeVar('T', int, str)"]
    D --> D3["Union constraint"]
```

**Diagram Explanation**: This diagram shows the different types of TypeVar constraints available in Python, from unconstrained to bounded and constrained type variables.

### Unconstrained TypeVar

```python
from typing import TypeVar

# Unconstrained type variable - any type allowed
T = TypeVar('T')

def identity(value: T) -> T:
    """Return the value unchanged."""
    return value

def first_item(items: list[T]) -> T:
    """Return the first item from a list."""
    return items[0]

# Usage with any type
print(identity(42))  # Output: 42 (int)
print(identity("hello"))  # Output: "hello" (str)
print(identity([1, 2, 3]))  # Output: [1, 2, 3] (list)

numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
print(first_item(numbers))  # Output: 1 (int)
print(first_item(names))    # Output: "Alice" (str)
```

### Bounded TypeVar

```python
from typing import TypeVar

# Bounded type variable - must be int or float
Numeric = TypeVar('Numeric', bound=int | float)

def add_numbers(a: Numeric, b: Numeric) -> Numeric:
    """Add two numeric values."""
    return a + b

def multiply_numbers(a: Numeric, b: Numeric) -> Numeric:
    """Multiply two numeric values."""
    return a * b

# ✅ Valid usage
result1 = add_numbers(5, 10)      # int + int = int
result2 = add_numbers(3.14, 2.71) # float + float = float
result3 = multiply_numbers(4, 2.5) # int * float = float

print(result1)  # Output: 15
print(result2)  # Output: 5.85
print(result3)  # Output: 10.0

# ❌ Invalid usage - would cause type error
# result4 = add_numbers("5", "10")  # Error: str not allowed
```

### Constrained TypeVar

```python
from typing import TypeVar

# Constrained type variable - only specific types allowed
StringOrNumber = TypeVar('StringOrNumber', str, int, float)

def process_value(value: StringOrNumber) -> str:
    """Process a value and return a string representation."""
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, (int, float)):
        return str(value * 2)
    else:
        raise TypeError("Unsupported type")

# ✅ Valid usage
print(process_value("hello"))  # Output: "HELLO"
print(process_value(42))       # Output: "84"
print(process_value(3.14))     # Output: "6.28"

# ❌ Invalid usage - would cause type error
# print(process_value([1, 2, 3]))  # Error: list not allowed
```

### Inheritance Bounds

```python
from typing import TypeVar

# Base class
class Animal:
    def make_sound(self) -> str:
        return "Some sound"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"

# TypeVar bounded to Animal and its subclasses
A = TypeVar('A', bound=Animal)

def make_animal_sound(animal: A) -> str:
    """Make an animal sound."""
    return animal.make_sound()

# Usage
dog = Dog()
cat = Cat()
animal = Animal()

print(make_animal_sound(dog))    # Output: "Woof!"
print(make_animal_sound(cat))    # Output: "Meow!"
print(make_animal_sound(animal)) # Output: "Some sound"
```

## Generic Collections

Python 3.12 supports inline generic syntax for collections, making them more readable and easier to use.

### Collection Syntax Comparison

```mermaid
graph TD
    A["Generic Collections"] --> B["Old Syntax"]
    A --> C["New Syntax (Python 3.12)"]
    
    B --> B1["List[T]"]
    B --> B2["Dict[K, V]"]
    B --> B3["Set[T]"]
    B --> B4["Tuple[T, ...]"]
    
    C --> C1["list[T]"]
    C --> C2["dict[K, V]"]
    C --> C3["set[T]"]
    C --> C4["tuple[T, ...]"]
```

**Diagram Explanation**: This diagram shows the comparison between old and new generic collection syntax in Python 3.12.

### Basic Generic Collections

```python
# Python 3.12 syntax for collections
from typing import Optional

# Generic lists
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]
scores: list[float] = [85.5, 92.0, 78.5]

# Generic dictionaries
person: dict[str, str] = {"name": "Alice", "email": "alice@example.com"}
scores_dict: dict[str, int] = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Generic sets
unique_names: set[str] = {"Alice", "Bob", "Charlie"}
unique_numbers: set[int] = {1, 2, 3, 4, 5}

# Generic tuples
coordinates: tuple[float, float] = (3.14, 2.71)
person_info: tuple[str, int, str] = ("Alice", 25, "alice@example.com")

# Optional types
optional_name: Optional[str] = None
optional_age: Optional[int] = 25
```

### Advanced Generic Collections

```python
from typing import Optional, Union

# Nested collections
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
people: list[dict[str, Union[str, int]]] = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Complex nested structures
api_responses: dict[str, list[dict[str, Union[str, int, bool]]]] = {
    "users": [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False}
    ],
    "products": [
        {"id": 1, "name": "Laptop", "price": 999},
        {"id": 2, "name": "Phone", "price": 599}
    ]
}

# Generic function with collections
def process_items[T](items: list[T]) -> list[T]:
    """Process a list of items."""
    return [item for item in items if item is not None]

def get_values[K, V](d: dict[K, V]) -> list[V]:
    """Get all values from a dictionary."""
    return list(d.values())

# Usage
numbers = [1, 2, 3, 4, 5]
processed = process_items(numbers)
print(processed)  # Output: [1, 2, 3, 4, 5]

person = {"name": "Alice", "age": 25}
values = get_values(person)
print(values)  # Output: ["Alice", 25]
```

### Generic Collection Classes

```python
class GenericList[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def add(self, item: T) -> None:
        """Add an item to the list."""
        self.items.append(item)
    
    def get(self, index: int) -> T:
        """Get an item by index."""
        return self.items[index]
    
    def remove(self, item: T) -> bool:
        """Remove an item from the list."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def size(self) -> int:
        """Get the size of the list."""
        return len(self.items)
    
    def __repr__(self) -> str:
        return f"GenericList({self.items})"

class GenericDict[K, V]:
    def __init__(self):
        self.items: dict[K, V] = {}
    
    def set(self, key: K, value: V) -> None:
        """Set a key-value pair."""
        self.items[key] = value
    
    def get(self, key: K) -> Optional[V]:
        """Get a value by key."""
        return self.items.get(key)
    
    def has_key(self, key: K) -> bool:
        """Check if a key exists."""
        return key in self.items
    
    def keys(self) -> list[K]:
        """Get all keys."""
        return list(self.items.keys())
    
    def values(self) -> list[V]:
        """Get all values."""
        return list(self.items.values())
    
    def __repr__(self) -> str:
        return f"GenericDict({self.items})"

# Usage
string_list = GenericList[str]()
string_list.add("hello")
string_list.add("world")
print(string_list)  # Output: GenericList(['hello', 'world'])

person_dict = GenericDict[str, int]()
person_dict.set("Alice", 25)
person_dict.set("Bob", 30)
print(person_dict.get("Alice"))  # Output: 25
print(person_dict.keys())        # Output: ['Alice', 'Bob']
```

## Overloading with @overload

Function overloading allows you to define multiple function signatures for different input types, providing better type safety and IDE support.

### Overloading Overview

```mermaid
graph TD
    A["Function Overloading"] --> B["Multiple Signatures"]
    A --> C["Type-Specific Behavior"]
    A --> D["Implementation"]
    
    B --> B1["@overload decorator"]
    B --> B2["Different parameter types"]
    B --> B3["Different return types"]
    
    C --> C1["Type checker uses signatures"]
    C --> C2["Runtime uses implementation"]
    C --> C3["Better type inference"]
    
    D --> D1["Single implementation"]
    D --> D2["Handles all cases"]
    D --> D3["Runtime behavior"]
```

**Diagram Explanation**: This diagram shows how function overloading works, with multiple signatures for type checking and a single implementation for runtime behavior.

### Basic Overloading

```python
from typing import overload

@overload
def process_value(x: int) -> int: ...

@overload
def process_value(x: str) -> str: ...

@overload
def process_value(x: list[int]) -> list[int]: ...

def process_value(x: int | str | list[int]) -> int | str | list[int]:
    """Process a value based on its type."""
    if isinstance(x, int):
        return x * 2
    elif isinstance(x, str):
        return x.upper()
    elif isinstance(x, list):
        return [item * 2 for item in x]
    else:
        raise TypeError("Unsupported type")

# Usage - type checker knows the return type
result1 = process_value(42)        # Type: int
result2 = process_value("hello")   # Type: str
result3 = process_value([1, 2, 3]) # Type: list[int]

print(result1)  # Output: 84
print(result2)  # Output: "HELLO"
print(result3)  # Output: [2, 4, 6]
```

### Advanced Overloading

```python
from typing import overload, Union

@overload
def parse_data(data: str) -> dict[str, str]: ...

@overload
def parse_data(data: list[str]) -> list[dict[str, str]]: ...

@overload
def parse_data(data: dict[str, str]) -> dict[str, str]: ...

def parse_data(data: str | list[str] | dict[str, str]) -> dict[str, str] | list[dict[str, str]]:
    """Parse data based on its type."""
    if isinstance(data, str):
        # Parse string as key=value pairs
        pairs = data.split(',')
        result = {}
        for pair in pairs:
            key, value = pair.split('=')
            result[key.strip()] = value.strip()
        return result
    elif isinstance(data, list):
        # Parse list of strings
        return [parse_data(item) for item in data]
    elif isinstance(data, dict):
        # Return dict as-is
        return data
    else:
        raise TypeError("Unsupported data type")

# Usage
string_data = "name=Alice,age=25,city=New York"
list_data = ["name=Bob,age=30", "name=Charlie,age=35"]
dict_data = {"name": "David", "age": "40"}

result1 = parse_data(string_data)  # Type: dict[str, str]
result2 = parse_data(list_data)    # Type: list[dict[str, str]]
result3 = parse_data(dict_data)    # Type: dict[str, str]

print(result1)  # Output: {'name': 'Alice', 'age': '25', 'city': 'New York'}
print(result2)  # Output: [{'name': 'Bob', 'age': '30'}, {'name': 'Charlie', 'age': '35'}]
print(result3)  # Output: {'name': 'David', 'age': '40'}
```

### Generic Overloading

```python
from typing import overload, TypeVar

T = TypeVar('T')

@overload
def transform(x: int) -> str: ...

@overload
def transform(x: str) -> int: ...

@overload
def transform(x: list[T]) -> list[T]: ...

def transform(x: int | str | list[T]) -> str | int | list[T]:
    """Transform a value based on its type."""
    if isinstance(x, int):
        return str(x)
    elif isinstance(x, str):
        return len(x)
    elif isinstance(x, list):
        return x[::-1]  # Reverse the list
    else:
        raise TypeError("Unsupported type")

# Usage
result1 = transform(42)        # Type: str
result2 = transform("hello")   # Type: int
result3 = transform([1, 2, 3]) # Type: list[int]

print(result1)  # Output: "42"
print(result2)  # Output: 5
print(result3)  # Output: [3, 2, 1]
```

## Real-World Examples

Let's explore practical examples of how generics are used in real-world applications.

### Example 1: API Response Wrapper

```python
from typing import Optional, Any
from datetime import datetime

class APIResponse[T]:
    def __init__(self, data: T, status_code: int, message: str = "Success", timestamp: Optional[datetime] = None):
        self.data = data
        self.status_code = status_code
        self.message = message
        self.timestamp = timestamp or datetime.now()
    
    def is_success(self) -> bool:
        """Check if the response indicates success."""
        return 200 <= self.status_code < 300
    
    def is_error(self) -> bool:
        """Check if the response indicates an error."""
        return not self.is_success()
    
    def get_data(self) -> T:
        """Get the response data."""
        if self.is_success():
            return self.data
        else:
            raise ValueError(f"API Error {self.status_code}: {self.message}")
    
    def to_dict(self) -> dict[str, Any]:
        """Convert response to dictionary."""
        return {
            "data": self.data,
            "status_code": self.status_code,
            "message": self.message,
            "timestamp": self.timestamp.isoformat()
        }
    
    def __repr__(self) -> str:
        return f"APIResponse(data={self.data}, status_code={self.status_code}, message='{self.message}')"

# Usage examples
user_response = APIResponse[dict](
    data={"id": 1, "name": "Alice", "email": "alice@example.com"},
    status_code=200
)

users_response = APIResponse[list](
    data=[
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ],
    status_code=200
)

error_response = APIResponse[None](
    data=None,
    status_code=404,
    message="User not found"
)

print(user_response.get_data())  # Output: {"id": 1, "name": "Alice", "email": "alice@example.com"}
print(users_response.get_data())  # Output: [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

try:
    error_response.get_data()  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: API Error 404: User not found
```

### Example 2: Caching System

```python
from typing import Optional, Callable, Any
import time
from datetime import datetime, timedelta

class Cache[K, V]:
    def __init__(self, default_ttl: int = 3600):  # 1 hour default TTL
        self.store: dict[K, tuple[V, datetime]] = {}
        self.default_ttl = default_ttl
    
    def set(self, key: K, value: V, ttl: Optional[int] = None) -> None:
        """Set a key-value pair with optional TTL."""
        ttl = ttl or self.default_ttl
        expiry = datetime.now() + timedelta(seconds=ttl)
        self.store[key] = (value, expiry)
    
    def get(self, key: K) -> Optional[V]:
        """Get a value by key if not expired."""
        if key not in self.store:
            return None
        
        value, expiry = self.store[key]
        if datetime.now() > expiry:
            del self.store[key]
            return None
        
        return value
    
    def get_or_set(self, key: K, factory: Callable[[], V], ttl: Optional[int] = None) -> V:
        """Get a value or set it using a factory function."""
        value = self.get(key)
        if value is None:
            value = factory()
            self.set(key, value, ttl)
        return value
    
    def delete(self, key: K) -> bool:
        """Delete a key from the cache."""
        if key in self.store:
            del self.store[key]
            return True
        return False
    
    def clear(self) -> None:
        """Clear all cached values."""
        self.store.clear()
    
    def size(self) -> int:
        """Get the number of cached items."""
        return len(self.store)
    
    def cleanup_expired(self) -> int:
        """Remove expired items and return count of removed items."""
        now = datetime.now()
        expired_keys = [key for key, (_, expiry) in self.store.items() if now > expiry]
        for key in expired_keys:
            del self.store[key]
        return len(expired_keys)

# Usage
cache = Cache[str, str](default_ttl=60)  # 1 minute default TTL

# Set values
cache.set("user:1", "Alice")
cache.set("user:2", "Bob", ttl=120)  # 2 minutes TTL

# Get values
print(cache.get("user:1"))  # Output: "Alice"
print(cache.get("user:2"))  # Output: "Bob"
print(cache.get("user:3"))  # Output: None

# Get or set with factory
def fetch_user_from_db(user_id: str) -> str:
    print(f"Fetching user {user_id} from database...")
    return f"User {user_id} from DB"

user = cache.get_or_set("user:3", lambda: fetch_user_from_db("3"))
print(user)  # Output: "Fetching user 3 from database..." then "User 3 from DB"

# Second call uses cache
user = cache.get_or_set("user:3", lambda: fetch_user_from_db("3"))
print(user)  # Output: "User 3 from DB" (no database call)
```

### Example 3: Generic Data Processing Pipeline

```python
from typing import TypeVar, Callable, Any, Optional
from abc import ABC, abstractmethod

T = TypeVar('T')
U = TypeVar('U')

class Processor[T, U](ABC):
    """Abstract base class for data processors."""
    
    @abstractmethod
    def process(self, data: T) -> U:
        """Process data and return transformed result."""
        pass

class StringProcessor(Processor[str, str]):
    """Process strings."""
    
    def process(self, data: str) -> str:
        return data.upper().strip()

class NumberProcessor(Processor[int, float]):
    """Process integers to floats."""
    
    def process(self, data: int) -> float:
        return float(data * 1.5)

class DataPipeline[T, U]:
    """Generic data processing pipeline."""
    
    def __init__(self):
        self.processors: list[Processor[Any, Any]] = []
    
    def add_processor[V](self, processor: Processor[U, V]) -> 'DataPipeline[T, V]':
        """Add a processor to the pipeline."""
        self.processors.append(processor)
        return self
    
    def process(self, data: T) -> Any:
        """Process data through all processors."""
        result = data
        for processor in self.processors:
            result = processor.process(result)
        return result
    
    def clear(self) -> None:
        """Clear all processors."""
        self.processors.clear()

# Usage
# String processing pipeline
string_pipeline = DataPipeline[str, str]()
string_pipeline.add_processor(StringProcessor())

result = string_pipeline.process("  hello world  ")
print(result)  # Output: "HELLO WORLD"

# Number processing pipeline
number_pipeline = DataPipeline[int, float]()
number_pipeline.add_processor(NumberProcessor())

result = number_pipeline.process(10)
print(result)  # Output: 15.0
```

## Best Practices

Following best practices ensures effective use of Pydantic and generics in your Python projects.

### Pydantic Best Practices

```mermaid
graph TD
    A["Pydantic Best Practices"] --> B["Model Design"]
    A --> C["Validation"]
    A --> D["Performance"]
    A --> E["Security"]
    
    B --> B1["Use type hints"]
    B --> B2["Keep models simple"]
    B --> B3["Use inheritance"]
    
    C --> C1["Custom validators"]
    C --> C2["Field validation"]
    C --> C3["Model validation"]
    
    D --> D1["Lazy validation"]
    D --> D2["Caching"]
    D --> D3["Efficient serialization"]
    
    E --> E1["Input sanitization"]
    E --> E2["Sensitive data"]
    E --> E3["Validation errors"]
```

**Diagram Explanation**: This diagram shows the key areas of best practices for Pydantic, including model design, validation, performance, and security.

### 1. Model Design

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# ✅ Good: Clear, well-typed models
class User(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=20)
    email: str = Field(regex=r'^[^@]+@[^@]+\.[^@]+$')
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    tags: List[str] = Field(default_factory=list)

# ✅ Good: Use inheritance for common fields
class BaseEntity(BaseModel):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

class Product(BaseEntity):
    name: str
    price: float = Field(gt=0)
    description: Optional[str] = None

class Category(BaseEntity):
    name: str
    description: Optional[str] = None
```

### 2. Validation Best Practices

```python
from pydantic import BaseModel, field_validator, model_validator
from typing import Optional
import re

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str
    age: int

    @field_validator("username")
    def validate_username(cls, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValueError("Username must contain only letters, numbers, and underscores")
        return value.lower()

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r'\d', value):
            raise ValueError("Password must contain at least one number")
        return value

    @model_validator(mode='after')
    def validate_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

### 3. Settings Management Best Practices

```python
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, List

class DatabaseSettings(BaseSettings):
    host: str = "localhost"
    port: int = Field(default=5432, ge=1, le=65535)
    username: str
    password: str
    database: str
    ssl_mode: bool = False

class APISettings(BaseSettings):
    title: str = "My API"
    version: str = "1.0.0"
    allowed_hosts: List[str] = ["localhost", "127.0.0.1"]
    cors_origins: List[str] = ["http://localhost:3000"]

class Settings(BaseSettings):
    # Nested settings
    database: DatabaseSettings = DatabaseSettings()
    api: APISettings = APISettings()
    
    # Environment-specific settings
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    secret_key: str = Field(..., min_length=32)
    
    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"
        case_sensitive = False
```

### Generics Best Practices

```mermaid
graph TD
    A["Generics Best Practices"] --> B["Type Safety"]
    A --> C["Code Reusability"]
    A --> D["Performance"]
    A --> E["Maintainability"]
    
    B --> B1["Use bounds"]
    B --> B2["Avoid Any"]
    B --> B3["Type constraints"]
    
    C --> C1["Generic functions"]
    C --> C2["Generic classes"]
    C --> C3["DRY principle"]
    
    D --> D1["No runtime overhead"]
    D --> D2["Efficient code"]
    D --> D3["Memory usage"]
    
    E --> E1["Clear documentation"]
    E --> E2["Consistent naming"]
    E --> E3["Error handling"]
```

**Diagram Explanation**: This diagram shows the key areas of best practices for generics, including type safety, code reusability, performance, and maintainability.

### 1. Type Safety

```python
from typing import TypeVar, Generic

# ✅ Good: Use bounds for type safety
Numeric = TypeVar('Numeric', bound=int | float)

def safe_add(a: Numeric, b: Numeric) -> Numeric:
    """Add two numeric values safely."""
    return a + b

# ✅ Good: Use constraints for specific types
StringOrNumber = TypeVar('StringOrNumber', str, int, float)

def process_value(value: StringOrNumber) -> str:
    """Process a value and return string representation."""
    return str(value)

# ❌ Bad: Avoid unconstrained generics when possible
T = TypeVar('T')

def unsafe_process(value: T) -> T:
    """This is too generic and unsafe."""
    return value  # What if T doesn't support the operation?
```

### 2. Code Reusability

```python
# ✅ Good: Generic data structures
class Stack[T]:
    def __init__(self):
        self.items: list[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        return self.items.pop()
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

# ✅ Good: Generic utility functions
def first_item[T](items: list[T]) -> T:
    """Get the first item from a list."""
    if not items:
        raise ValueError("List is empty")
    return items[0]

def last_item[T](items: list[T]) -> T:
    """Get the last item from a list."""
    if not items:
        raise ValueError("List is empty")
    return items[-1]
```

### 3. Performance Considerations

```python
# ✅ Good: Use built-in collections when possible
def process_items[T](items: list[T]) -> list[T]:
    """Process items efficiently."""
    return [item for item in items if item is not None]

# ✅ Good: Avoid unnecessary type checking at runtime
def add_numbers[T: int | float](a: T, b: T) -> T:
    """Add numbers without runtime type checking."""
    return a + b  # Type checker ensures T is numeric

# ❌ Bad: Don't do runtime type checking in generic functions
def bad_add[T](a: T, b: T) -> T:
    """This defeats the purpose of generics."""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Unsupported types")
```

### 4. Documentation and Naming

```python
from typing import TypeVar, Generic, Optional

# ✅ Good: Clear type variable names
KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')
ItemType = TypeVar('ItemType')

# ✅ Good: Well-documented generic classes
class Cache[KeyType, ValueType](Generic[KeyType, ValueType]):
    """
    A generic cache implementation.
    
    Args:
        KeyType: The type of keys used in the cache
        ValueType: The type of values stored in the cache
    """
    
    def __init__(self, max_size: int = 100):
        self.max_size = max_size
        self.store: dict[KeyType, ValueType] = {}
    
    def get(self, key: KeyType) -> Optional[ValueType]:
        """Get a value from the cache."""
        return self.store.get(key)
    
    def set(self, key: KeyType, value: ValueType) -> None:
        """Set a value in the cache."""
        if len(self.store) >= self.max_size:
            # Remove oldest item (simple implementation)
            oldest_key = next(iter(self.store))
            del self.store[oldest_key]
        self.store[key] = value
```

## Key Concepts Summary

This comprehensive lesson covered two powerful Python features for modern development: Pydantic for data validation and Generics for type-safe, reusable code.

### Pydantic Summary

- **Definition**: Python library for data validation and settings management using type hints
- **Key Features**: Automatic validation, JSON serialization, settings management, custom validators
- **Use Cases**: API validation, configuration management, data parsing, environment variables
- **Best Practice**: Use for data-oriented applications requiring validation and serialization

### Generics Summary

- **Definition**: Type parameterization system that allows writing reusable, type-safe code
- **Key Features**: Type safety, code reusability, better syntax in Python 3.12, enhanced error messages
- **Use Cases**: Generic data structures, API responses, caching systems, data processing pipelines
- **Best Practice**: Use for creating reusable components that work with multiple types

### Key Benefits

| Feature | Pydantic | Generics |
|---------|----------|----------|
| **Type Safety** | Runtime validation | Compile-time checking |
| **Code Reusability** | Model inheritance | Generic functions/classes |
| **Performance** | Validation overhead | No runtime overhead |
| **Use Case** | Data validation | Type-safe code reuse |
| **Learning Curve** | Moderate | Moderate to High |

### Decision Matrix

| Need | Use |
|------|-----|
| Data validation | Pydantic |
| Settings management | Pydantic |
| API request/response | Pydantic |
| Generic data structures | Generics |
| Type-safe functions | Generics |
| Code reusability | Generics |
| Configuration files | Pydantic |
| Data processing pipelines | Generics |

## Useful Links

### Documentation and References

- [Pydantic Official Documentation](https://docs.pydantic.dev/)
- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [PEP 557 - Data Classes](https://peps.python.org/pep-0557/)
- [PEP 695 - Type Parameter Syntax](https://peps.python.org/pep-0695/)
- [Python 3.12 What's New](https://docs.python.org/3/whatsnew/3.12.html)

### Advanced Topics

- [Pydantic V2 Migration Guide](https://docs.pydantic.dev/2.0/migration/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Generic Types in Python](https://docs.python.org/3/library/typing.html#generics)
- [Function Overloading](https://docs.python.org/3/library/typing.html#typing.overload)

### Best Practices

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [Python Best Practices](https://docs.python-guide.org/)

### Tools and Libraries

- [mypy - Static Type Checker](https://mypy.readthedocs.io/)
- [pydantic-settings](https://docs.pydantic.dev/2.0/usage/settings/)
- [FastAPI - Modern Web Framework](https://fastapi.tiangolo.com/)
- [pydantic[email] - Email Validation](https://docs.pydantic.dev/2.0/usage/types/extra_types/)

---

## Conclusion

This lesson covered two essential Python features for modern development:

### Pydantic
- **Data validation powerhouse** - Ensures data integrity and type safety
- **Settings management** - Perfect for configuration and environment variables
- **JSON serialization** - Easy conversion between Python objects and JSON
- **Custom validation** - Flexible validation rules for complex business logic

### Generics
- **Type-safe code reuse** - Write once, use with multiple types
- **Python 3.12 improvements** - Cleaner syntax and better error messages
- **Generic data structures** - Stacks, queues, caches that work with any type
- **Function overloading** - Multiple signatures for different input types

### Key Takeaways

1. **Pydantic ensures data integrity** - Use for validation, settings, and serialization
2. **Generics enable type-safe reuse** - Use for creating reusable, type-safe components
3. **Python 3.12 makes generics easier** - New syntax is cleaner and more readable
4. **Combine both for powerful applications** - Pydantic for data, generics for code reuse
5. **Follow best practices** - Type safety, validation, and clear documentation

### When to Use Each

**Use Pydantic when:**
- Building APIs that need request/response validation
- Managing configuration files and environment variables
- Parsing and validating external data
- Creating data models with validation rules

**Use Generics when:**
- Creating reusable data structures (stacks, queues, caches)
- Writing functions that work with multiple types
- Building type-safe libraries and frameworks
- Implementing design patterns with type safety

### Final Thoughts

Both Pydantic and Generics represent the evolution of Python toward more robust, type-safe development. They enable you to write code that is:

- **More reliable** - Type checking catches errors early
- **More maintainable** - Clear interfaces and validation
- **More reusable** - Generic components work with multiple types
- **More professional** - Industry-standard tools for modern Python development

Remember: **Good Python code is type-safe, well-validated, and reusable. Pydantic and Generics are powerful tools that help you achieve these goals while maintaining Python's simplicity and readability.**

---