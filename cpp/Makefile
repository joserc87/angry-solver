
ALL: angrySolver

angrySolver: main.o CTreeNode.o CDictionary.o CAngryWordsBoard.o
	g++ -g -o angrySolver main.o CTreeNode.o CDictionary.o CAngryWordsBoard.o

main.o: main.cpp
	g++ -g -c -o main.o main.cpp

CTreeNode.o: CTreeNode.cpp CTreeNode.hpp
	g++ -g -c -o CTreeNode.o CTreeNode.cpp

CDictionary.o: CDictionary.cpp CDictionary.hpp
	g++ -g -c -o CDictionary.o CDictionary.cpp

CAngryWordsBoard.o: CAngryWordsBoard.cpp CAngryWordsBoard.hpp
	g++ -g -c -o CAngryWordsBoard.o CAngryWordsBoard.cpp
