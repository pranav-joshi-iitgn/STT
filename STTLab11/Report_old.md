# STT Lab 11

### Game Selection

The two games I’ve selected are

1. Snake  
2. Tetris

Just by playing the games and going over the source code, I’ve noticed these issues :

#### Snake

1. Escape key doesn’t work when selecting speed  
2. The perceived speed of the snake is more when it is moving vertically. This is because it moves by one line in one frame, while moving horizontally, it is one character. Since the `>` characters are meshed together on a line, the speed is lower visually.  
3. Resizing the console window automatically closes the game without specifying why it did that.  
4. No score is mentioned when the game closes upon a loss. This is problematic because there is actually code to handle that in the `.cs` file, but it is not being triggered. The same with the 3rd bug.  
5. The boundaries are not textually printed on the console. This is a problem when the console application has margins that merge into the space for text visually. 

#### Tetris

1. When the console is too small, the game tells the user to expand it, but does not react to either the expansion, or the user pressing enter key  
2. When the game tells the user to expand the screen, if the user expands and presses `<` or `>` then the game starts again. But if the user presses “Enter” and then `>` or `<` , the game shows an invalid state on the console with multiple boxes, the last one in “paused” state.  
3. Pressing the spacebar drops the block, and then holding the spacebar key further temporarily pauses the game. In this state.  
4. When the game is paused due to space bar key hold, the user can press another key, such as `>` or `<` which will perform its action and then restart the game. Releasing the space bar has no effect on the game. This means that the user can shift the block when it is dropped to the left or right by one step. This is usually done by mastering timing, so it is, in a way, cheating the system.

Since I could not find any more bugs, I introduced some myself, giving this as the final list of bugs in the code :

#### Snake

1. Escape key doesn’t work when selecting speed  
2. The perceived speed of the snake is more when it is moving vertically.  
3. Resizing the console window automatically closes the game without specifying why it did that.  
4. No score is mentioned when the game closes upon a loss. This is problematic because there is actually code to handle that in the `.cs` file, but it is not being triggered. The same with the 3rd bug.  
5. The snake moves up when the down arrow key is pressed and down when the up arrow key is pressed.

#### Tetris

1. When the console is too small, the game tells the user to expand it, but does not react to either the expansion, or the user pressing enter key  
2. When the game tells the user to expand the screen, if the user expands and presses `<` (right arrow key) or `>` then the game starts again. But if the user presses the Enter key and then `>` or `<` , the game shows an invalid state on the console with multiple boxes, the last one in “paused” state.  
3. Pressing the spacebar drops the block, and then holding the spacebar key further temporarily pauses the game. In this state.  
4. When the game is paused due to space bar key hold, the user can press another key, such as `>` or `<` which will perform its action and then restart the game. Releasing the space bar has no effect on the game. This means that the user can shift the block when it is dropped to the left or right by one step. This is usually done by mastering timing, so it is, in a way, cheating the system.  
5. The actions of `Q` and `E` are now printed incorrectly in the main menu

