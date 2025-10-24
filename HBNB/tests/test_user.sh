#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

BASE_URL="http://localhost:5000/api/v1"

echo "======================================"
echo "Testing HBnB User Endpoints"
echo "======================================"

# Test 1: Create a new user
echo -e "\n${YELLOW}Test 1: Create a new user (POST)${NC}"
RESPONSE=$(curl -s -X POST $BASE_URL/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}')
echo "Response: $RESPONSE"
USER_ID=$(echo $RESPONSE | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
echo -e "${GREEN}✓ User created with ID: $USER_ID${NC}"

# Test 2: Get user by ID
echo -e "\n${YELLOW}Test 2: Get user by ID (GET)${NC}"
RESPONSE=$(curl -s -X GET $BASE_URL/users/$USER_ID)
echo "Response: $RESPONSE"
if [[ $RESPONSE == *"$USER_ID"* ]]; then
  echo -e "${GREEN}✓ User retrieved successfully${NC}"
else
  echo -e "${RED}✗ Failed to retrieve user${NC}"
fi

# Test 3: Get all users
echo -e "\n${YELLOW}Test 3: Get all users (GET)${NC}"
RESPONSE=$(curl -s -X GET $BASE_URL/users/)
echo "Response: $RESPONSE"
if [[ $RESPONSE == *"$USER_ID"* ]]; then
  echo -e "${GREEN}✓ All users retrieved successfully${NC}"
else
  echo -e "${RED}✗ Failed to retrieve all users${NC}"
fi

# Test 4: Update user
echo -e "\n${YELLOW}Test 4: Update user (PUT)${NC}"
RESPONSE=$(curl -s -X PUT $BASE_URL/users/$USER_ID \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}')
echo "Response: $RESPONSE"
if [[ $RESPONSE == *"Jane"* ]]; then
  echo -e "${GREEN}✓ User updated successfully${NC}"
else
  echo -e "${RED}✗ Failed to update user${NC}"
fi

# Test 5: Duplicate email
echo -e "\n${YELLOW}Test 5: Try duplicate email (should fail)${NC}"
RESPONSE=$(curl -s -X POST $BASE_URL/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Test", "last_name": "User", "email": "jane.doe@example.com"}')
echo "Response: $RESPONSE"
if [[ $RESPONSE == *"Email already registered"* ]]; then
  echo -e "${GREEN}✓ Duplicate email correctly rejected${NC}"
else
  echo -e "${RED}✗ Should have rejected duplicate email${NC}"
fi

# Test 6: User not found
echo -e "\n${YELLOW}Test 6: Get non-existent user (should return 404)${NC}"
RESPONSE=$(curl -s -X GET $BASE_URL/users/fake-id-123)
echo "Response: $RESPONSE"
if [[ $RESPONSE == *"User not found"* ]]; then
  echo -e "${GREEN}✓ 404 correctly returned${NC}"
else
  echo -e "${RED}✗ Should have returned 404${NC}"
fi

echo -e "\n======================================"
echo -e "${GREEN}All tests completed!${NC}"
echo "======================================"