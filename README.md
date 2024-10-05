# Hierarchical Task Management App
## Overall Goal
The application should allow users to create multiple lists, and each list should be able to contain multiple items. Each item should be able to contain multiple sub-items, and so on. The user should be able to create, edit, and delete lists and items. The user should also be able to move items between lists.

Your visual design can be very straightforward. In practice, a true recursive solution is difficult to style in a way that is both visually appealing and easy to use. For this reason, you are allowed to limit the depth of the hierarchy to 3 levels. (This means that each list can contain items, and each item can contain sub-items, and each sub-item can contain sub-sub-items, but no further.)

The true value of a hierarchical todo list is that it allows users to hide the sub-items of a given item. This allows users to focus on the most important tasks, and to hide the details until they are ready to deal with them. For this reason, your application should allow users to hide and show the sub-items of any item.
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
