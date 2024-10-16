# Hierarchical Task Management App
> Great code is the result of clear thinking.
## Step 1: Break the UI into a component hierarchy
In the component structure below, components on the same level of the tree have the same color.
![User Flow - Kanban Board (10)](https://github.com/user-attachments/assets/9131c812-500e-4769-9f67-a2fc44579f4b)

![User Flow - Kanban Board (11)](https://github.com/user-attachments/assets/d5be077f-786a-49a1-b9a5-e2dfaf79bb7e)

## Step 2: Build a static version in React

## Step 3: Find the minimal but complete representation of UI state

## Step 4: Identify where your state should live

## Step 5: Add inverse data flow 

## Requirements
- The app should have multiple users. Each user should only see their own tasks.
- Users should not be able to modify any other user's tasks.
- Forgot password functionality is not required.
- Users should be able to mark tasks as complete. (This can either hide the task or delete it entirely.)
- Users should be able to collapse (or expand) a task. This means that all subtasks are hidden from (or shown to) the user.
- Users should be able to move a top-level task to a different list. (No other permutation is required; for example, moving a sub-sub-task to a sub-task is too complicated for an MVP.)
- Your data should be saved somewhere durable, but the exact schema/approach is not important for this assignment. Sqlalchemy is recommended, but Firebase, MongoDB, etc, are also all fine choices.

## Extensions
- Allow the todo items to be infinitely nested and ensure that they render nicely to the screen. (Nice here is relative - pretty much any representation that is 10 layers deep will look awful. Just make sure that all the text is visible, and the columns are of a reasonable width)
- Allow each user to move tasks/subtasks around arbitrarily.
- Test your code! Unit tests are the best.

## Personal Notes
- React component functions accept a single argument, a `props` object
- Do not use indexes, `Math.random()` to generate keys.

## Useful Resources
1. https://react.dev/learn/thinking-in-react
