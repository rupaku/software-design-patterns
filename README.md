# software-design-patterns
software-design-patterns using Python

---
1. Creational Design Pattern
2. Structural Design Pattern
3. Behavioural Design Pattern


- ## **Creational Design Pattern**

<details>  
<summary>Structural Design Pattern </summary>
  
  Structural design patterns are a category of design patterns that focus on how objects and classes are composed to form larger structures. They help ensure that if one part of a system changes, the entire system     doesn’t need to change, promoting flexibility and efficiency.

  ### **Pros and Cons**
  Structural design patterns come with their own set of advantages and disadvantages. Here's a breakdown of the pros and cons:

  <details>  
  <summary>Pros</summary>
    
  - **Flexibility and Reusability:**
  
    Promote the reuse of existing components by allowing them to work together, even if their interfaces are incompatible.
  - **Decoupling**:
  
    Help decouple interfaces from implementations, making it easier to change one without affecting the other. This leads to more maintainable code.
  - **Scalability**:
  
    Support the addition of new functionalities without altering existing code, making it easier to scale applications.
  - **Improved Collaboration**:
  
    Facilitate collaboration between different systems and classes that may not have been designed to work together.
  - **Clearer Structure**:
  
    Provide a clear way to organize code, especially in complex systems, which enhances readability and understanding.
  </details>  
  <details>
  <summary>Cons</summary>
    
  - **Complexity:**
  
    Can introduce additional layers of abstraction, which may make the system more complex and harder to understand, especially for new developers.
  - **Performance Overhead:**
  
    The added layers (like adapters) can introduce performance overhead, which may be critical in performance-sensitive applications.
  - **Learning Curve:**
  
    Understanding and implementing structural patterns may require a deeper understanding of design principles, which can pose a challenge for less experienced developers.
  - **Over-Engineering:**
  
    There’s a risk of over-engineering a solution by introducing patterns that may not be necessary for simpler problems.
  - **Maintenance:**
  
    If not used judiciously, the added complexity can lead to maintenance challenges, particularly if the patterns are misapplied or overused.
    </details>

    <details>
      <summary>Adapter Design Pattern</summary>

      The Adapter Design Pattern is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two different interfaces, enabling them to communicate and               function as if they were compatible.
  
      - **Key Concepts**
        - Target Interface: This is the interface that the client expects. It defines the operations that the client can call.
      
        - Adaptee: This is the existing class with an incompatible interface. It has functionality that the client needs, but it doesn’t match the expected interface.
      
        - Adapter: This is the class that implements the target interface and translates calls to the adaptee's interface. The adapter makes the adaptee’s interface compatible with the target interface.
      
      - **Structure**
      
          Client
            |
          Target Interface
            |
           Adapter
            |
          Adaptee
        
        **Example Scenario**
      Imagine you have a legacy system that provides temperature readings in Fahrenheit, but you need a system that works with temperature readings in Celsius.
      
      1. Target Interface:
      ```class Temperature:
          def get_temperature(self) -> float:
              pass
      2. Adaptee:
        class FahrenheitThermometer:
          def get_fahrenheit(self) -> float:
              # Returns temperature in Fahrenheit
              return 100.0  # example value
      3. Adapter:
        class CelsiusAdapter(Temperature):
          def __init__(self, thermometer: FahrenheitThermometer):
              self.thermometer = thermometer
          def get_temperature(self) -> float:
              # Convert Fahrenheit to Celsius
              fahrenheit = self.thermometer.get_fahrenheit()
              return (fahrenheit - 32) * 5.0 / 9.0
         
      Client Code
      
        def print_temperature(temp: Temperature):
          print(f"The temperature is {temp.get_temperature()}°C.")
      
      # Usage
        fahrenheit_thermometer = FahrenheitThermometer()
        adapter = CelsiusAdapter(fahrenheit_thermometer)
        
        print_temperature(adapter)  # Outputs the temperature in Celsius```

    
      - **Benefits**
        Decoupling: The client code is decoupled from the specific implementation of the adaptee, allowing easier modifications.
        Reusability: You can use existing classes without modifying their code.
        Flexibility: You can introduce new classes without affecting the client, as long as they adhere to the target interface.
      
      - **When to Use**
        When you want to use some existing code, but its interface does not match the one you need.
        When you want to create a reusable class that cooperates with unrelated or unforeseen classes.
        The Adapter Pattern is a powerful way to integrate disparate systems and enhance the functionality of existing code with minimal disruption.
    </details>
    </details>
  </details>
    
