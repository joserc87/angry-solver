/**
 * @file common.h
 * common definitions
 */

#ifndef __COMMON_H__
#define __COMMON_H__
#include <string>

using namespace std;

#define EMPTY ' '
#define MAX_STRING 50

enum Direction {
  DOWN,
  RIGHT,
  UP,
  LEFT
};

struct AngryWordsMove{
  unsigned int row;
  unsigned int column;
  Direction direction;
  unsigned int score;
  string word;
  string lettersUsed;
  bool valid;
};

#endif // #ifndef __COMMON_H__

