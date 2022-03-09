using System;

namespace TicTacToe
{
    class Game
    {
        private char[,] Board;

        public Game()
        {
            Board = new char [3, 3] {{'_','_','_'},{'_','_','_'},{'_','_','_'}};
            InputFunc();
        }

        public void InputFunc()
        {
            for (int i = 1; i <= 9; i++)
            {
                int position;
                char temp;
                int player;
                if ( i % 2 != 0)
                {
                    position = GetPosition(1);
                    temp = 'X';
                    player = 1;
                }
                else
                {
                    position = GetPosition(2);
                    temp = 'O';
                    player = 2;
                }
                int row = position / 3;
                int col = position % 3;

                Board [row, col] = temp;
                Print2D(Board);

                var winner = CheckWinner(player);
                if (winner == true)
                {
                    Console.WriteLine("Player"+ player + " is the winner");
                    return;
                }
            }
        }

        private int GetPosition (int player)
        {
            if (player == 1)
            {
                Console.Write("Player1 - enter your position number between 1 and 9:");
                int num1 = Convert.ToInt32(Console.ReadLine());
                if ( num1 <= 0 || num1 > 9)
                {
                    Console.WriteLine("Input must be between 1 and 9");
                }
                return (num1-1);
            }
            else
            {
                Console.Write("Player2 - enter your position number between 1 and 9:");
                int num2 = Convert.ToInt32(Console.ReadLine());
                if ( num2 <= 0 || num2 > 9)
                {
                    Console.WriteLine("Input must be between 1 and 9");
                }
                return (num2 - 1);
            }
        }

        public void Print2D (char[,] Arr1)
        {
            for (int i = 0; i < Arr1.GetLength(0); i++)
            {
                for (int j = 0; j < Arr1.GetLength(1); j++)
                {
                    Console.Write(Arr1[i, j] + " ");
                }
                Console.Write('\n');
            }
     
        }

        private bool CheckWinner(int player)
        {
            var a = CheckWinnerRow(0, player);
            var b = CheckWinnerRow(1, player);
            var c = CheckWinnerRow(2, player);

            var d = CheckWinnerRow(0, player);
            var e = CheckWinnerRow(1, player);
            var f = CheckWinnerRow(2, player);

            var g = CheckDiagonal1(player);

            var h = CheckDiagonal2(player);

            if (a == true || b==true  || c==true || d==true || e==true || f==true || g==true || h==true)
            {
                return true;
            }
            else
            {
                return false;
            }
        } 

        private bool CheckWinnerRow(int row, int player)
        {
            char temp;
            if (player == 1)
            {
            temp = 'X';              
            }
            else
            {
                temp = 'O';            
            }
            if( Board[row,0] == temp && Board[row,1] == temp && Board[row,2] == temp)
            {
                return true;
            }
            else
            {
                return false;
            }      
        }

        private bool CheckWinnerCol(int col, int player)
        {
            char temp;
            if (player == 1)
            {
            temp = 'X';            
            }
            else
            {
                temp = 'O';     
            }
            if( Board[0,col] == temp && Board[1,col] == temp && Board[2,col] == temp)
            {
                return true;
            }
            else
            {
                return false;
            }     
        }


        private bool CheckDiagonal1(int player)
        {
            char temp;
            if (player == 1)
            {
                temp = 'X';   
            }
            else
            {
                temp = 'O';
            }
            if (Board[0,0] == temp && Board[1,1] == temp && Board[2,2] == temp)
            {
                return true;
            }
            else
            {
                return false;
            }    
        }


         private bool CheckDiagonal2(int player)
        {
            char temp;
            if (player == 1)
            {
                temp = 'X';   
            }
            else
            {
                temp = 'O';
            }
            if (Board[0,2] == temp && Board[1,1] == temp && Board[2,0] == temp)
            {
                return true;
            }
            else
            {
                return false;
            }    
        }
    }       
}

