#include "iostream"
#include "fstream" 
#include <sstream>
#include <string>
void FileReader(char* path, int count){
    char* result;
    std::fstream f(path);
    if (!f.is_open()){
        std::cout<<"Failed open"<<std::endl;
    }
   else{
    std::string line;
    while (std::getline(f,line)){
    int d = 1024;
    f.read(reinterpret_cast<char*>(&d), sizeof d);
    f>>result;
    }


   }

   Counter(result,  count );

}
int Counter(char *result, int count){
    char original_key[size_t(result)] = {0};
    for (int i = 0; i < size_t(result); i++){
        for (int j = 0; i < size_t(result); i++){
            if (result[i] == original_key[j]){
                break;
            }
            else if (original_key[j] == 0){
                original_key[j] = result[i];
            }
        }
    }
    int count_massive[size_t(result)] = {0};
    for (int k = 0 ; k < size_t(result); k++){
        int count_pov = 0;
        for (int l = 0 ; l < size_t(result); l++){
            if (result[l] == original_key[k] ){
                count_pov++;
            } 
        }
        count_massive[k] = count_pov;
    }
    int max_zn = -999;
    int current_index = 0;
    for (count ; count>0; count--){
        for (int r = 0; r < size_t(count_massive); r++){
            if (max_zn < count_massive[r]){
                max_zn = count_massive[r];
                current_index = r;
            }
        }
        std::cout<<original_key[current_index];
        original_key[current_index] = {0};
    }
}


int main(int argc, char** argv){
char* path;
int count;
if (argc< 2) {
    std::cout<<"Eror: arguments "<<std::endl;
}
for (int i = 0; i < argc ; i++){
    if (argv[i] == "--input"){
        path = argv[i] + 1;
    }
    else if (argv[i] == "--top"){
        count = std::stoi(argv[i] + 1);
    }
}

FileReader(path,count);

return 0;
};