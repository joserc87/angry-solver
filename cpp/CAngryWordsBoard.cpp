
#include "CAngryWordsBoard.hpp"
#include <assert.h>

/**************************************************************************************************/
/**************************************************************************************************/

CAngryWordsBoard::CAngryWordsBoard (){
  const char *myBoard [15] = {
    "               ", // 0
    "               ",
    "       afeo    ",
    "       c       ",
    "       r       ",
    "    ujier      ", // 5
    "       c       ",
    "       i       ",
    "       o       ",
    "               ",
    "               ", // 10
    "               ",
    "               ",
    "               ",
    "               " // 14
  };
  for (int i=0; i<15; i++){
    for (int j=0; j<15; j++){
      board [i][j] = myBoard[i][j];
    }
  }
  // TODO: Change multipliers
  for (int i=0; i<15; i++){
    for (int j=0; j<15; j++){
      multipliers [i][j] = 1;
    }
  }
}

/**************************************************************************************************/
/**************************************************************************************************/

CAngryWordsBoard::~CAngryWordsBoard (){
  // We dont have to free anything
}

/**************************************************************************************************/
/**************************************************************************************************/

AngryWordsMove CAngryWordsBoard::findBestMove (const CDictionary &dic, string myLetters){
  AngryWordsMove move;
  move.valid=false;
  // for each position
  for (int i=0; i<BOARD_HEIGHT; i++){
    for (int j=0; j<BOARD_WIDTH; j++){
      // For each direction, (RIGHT and DOWN)
      // Check the best convination
      list <AngryWordsMove> moves = findAllMovesIn (i, j, RIGHT, myLetters, dic);
      for (list <AngryWordsMove>::const_iterator iter = moves.begin (); iter != moves.end (); iter++){
	move = maxMove (move, *iter);
      }
      moves = findAllMovesIn (i, j, DOWN, myLetters, dic);
      for (list <AngryWordsMove>::const_iterator iter = moves.begin (); iter != moves.end (); iter++){
	move = maxMove (move, *iter);
      }
    }
  }
  return move;
}

/**************************************************************************************************/
/**************************************************************************************************/

list<AngryWordsMove> CAngryWordsBoard::findAllMovesIn (unsigned short row, unsigned short column, Direction direction, string myLetters, const CDictionary &dic){
  list<AngryWordsMove> moves;
  // First of all, check that there can be a valid move at this position
  if (!checkNeighbours(row, column, direction, myLetters.length())){
    return (moves);
  }
  // Otherwise, if possible, lets start searching
  // First, take the row/column from the board, as a string
  string boardString = getStringFromBoard (row, column, direction);

  // Find a word that fits in the string
  // This is the main method of the algorithm
  list <string> words = dic.findWordsInPattern (boardString, myLetters);
  // Once we have the solutions, lets create the moves
  for (list<string>::const_iterator iter = words.begin (); iter != words.end (); iter++){
    string word = *iter;
    AngryWordsMove move;
    move.valid = true;
    move.row = row;
    move.column = column;
    move.direction = direction;
    move.score = calcScore (row, column, direction, word);
    move.word = word;
    move.lettersUsed = getLettersUsed (word, boardString);
  }
}

/**************************************************************************************************/
/**************************************************************************************************/

string CAngryWordsBoard::getStringFromBoard (unsigned short row, unsigned short column, Direction direction){
  unsigned short dx = 0, dy = 0;
  switch (direction){
  case RIGHT:
    dx = 1;
    break;
  case LEFT:
    dx = -1;
    break;
  case DOWN:
    dy = 1;
    break;
  case UP:
    dy = -1;
    break;
  }
  unsigned short i=row, j=column;
  bool end=false;
  char boardString [BOARD_WIDTH+1];
  unsigned short n=0;
  while (!end){
    // Check if finish
    if (i>=BOARD_HEIGHT || j>=BOARD_WIDTH){
      end = true;
    }else{
      // Add the character to the string
  boardString [n]= elementAt(i, j);
      // Advance
      i+=dy;
      j+=dx;
      n++;
    }  
  }
  boardString [n] = '\0';
  string str = boardString;
  return str;
}

/**************************************************************************************************/
/**************************************************************************************************/

short int CAngryWordsBoard::calcScore (unsigned short row, unsigned short column, Direction direction, string word){
  // TODO: This is not the real score, just a very bad stimation
  return word.length ();
}

/**************************************************************************************************/
/**************************************************************************************************/

bool CAngryWordsBoard::checkNeighbours(unsigned short row, unsigned short column, Direction direction, unsigned short length){
  unsigned short dx = 0, dy = 0;
  switch (direction){
  case RIGHT:
    dx = 1;
    break;
  case LEFT:
    dx = -1;
    break;
  case DOWN:
    dy = 1;
    break;
  case UP:
    dy = -1;
    break;
  }
  unsigned short i=row, j=column;
  for (unsigned short n = 0; n<length && i<BOARD_HEIGHT && j<BOARD_WIDTH; n++){
    if (elementAt(i, j) != EMPTY){
      return true;
    }
    i += dy;
    j += dx;
  }
  return false;
}

/**************************************************************************************************/
/**************************************************************************************************/

char CAngryWordsBoard::elementAt (unsigned short i, unsigned short j){
  assert (i<BOARD_HEIGHT && j<BOARD_WIDTH);
  return board [i][j];
}

/**************************************************************************************************/
/**************************************************************************************************/

AngryWordsMove CAngryWordsBoard::maxMove(AngryWordsMove m1, AngryWordsMove m2){
  if (!m2.valid){
    return m1;
  }else{
    if (!m1.valid || m2.score>m1.score){
      return m2;
    }else{
      return m1;
    }
  }
  return m1;
}

/**************************************************************************************************/
/**************************************************************************************************/

string CAngryWordsBoard::getLettersUsed (string word, string pattern){
  // To calc the letters used, substract the pattern from the word
  int n=0;
  char sub [BOARD_WIDTH];
  for (unsigned short i=0; i<word.length (); i++){
    if (pattern [i] == EMPTY){
      sub [n] = word [i];
    }
  }
  string letters = sub;
  return letters;
}

/**************************************************************************************************/
/**************************************************************************************************/
