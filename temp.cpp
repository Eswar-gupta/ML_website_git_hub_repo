#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include<algorithm>
#include<map>
using namespace std;

int main() {
    // Vectors to store the two columns
    std::vector<int> column1, column2;

    // Input file stream
    std::ifstream inputFile("input.txt");

    // Check if the file opened successfully
    if (!inputFile) {
        std::cerr << "Error: Unable to open file input.txt" << std::endl;
        return 1;
    }

    std::string line;
    // Read the file line by line
    while (std::getline(inputFile, line)) {
        std::istringstream lineStream(line);
        int num1, num2;

        // Read two integers from the line
        if (lineStream >> num1 >> num2) {
            column1.push_back(num1);
            column2.push_back(num2);
        }
    }

    inputFile.close();


    map<int,int> counter;
    for(int i = 0; i < column1.size(); i++) {
        counter[column1[i]]++;
    }
    
    long int ans = 0;

    for(int i = 0; i < column1.size(); i++) {
        ans += column2[i]*counter[column2[i]];
    }
    cout << ans << endl;
    return 0;
}
