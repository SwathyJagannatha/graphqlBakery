Building a Bakery Inventory Management GraphQL API
Objective: The objective of this assignment is to develop a GraphQL API for managing inventory data of a bakery. By completing this assignment, you will gain practical experience in building GraphQL APIs using Python and managing inventory data.

Problem Statement: Your task is to create a GraphQL API that allows users to query, add, update, and delete bakery inventory items. The inventory items include details such as product name, price, quantity, and category. This assignment will help you understand how to implement CRUD (Create, Read, Update, Delete) operations using GraphQL.

Task 1: Create a new file named schema.py and define the GraphQL schema to handle bakery inventory management.

Task 2: Create a new file named app.py and set up a Flask server to serve the GraphQL API. Define routes to expose the GraphQL endpoint and enable the GraphiQL interface for testing.

Task 3: Test the GraphQL API by accessing the GraphiQL interface in a web browser. Write sample queries and mutations to interact with the bakery inventory data, including fetching products, adding new products, updating product details, and deleting products.

Here’s an example:

query {
  products {
    id
    name
    price
    quantity
    category
  }
}
Expected Outcomes:

Upon completing this assignment, you should have successfully developed a GraphQL API for managing inventory data of a bakery. The API should support CRUD operations for bakery products and be accessible via the GraphiQL interface for testing and exploration.