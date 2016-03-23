#include <iostream>

#include <tesseract/baseapi.h>
#include <tesseract/strngs.h>

#include <leptonica/allheaders.h>

int main(int count, char** string) {


if (count < 2) {
 std::cout << "empty img_path" << std::endl;
 return -1;
}


const char* lan = "eng";
const char* img_path = string[1];

tesseract::TessBaseAPI *ocr = new tesseract::TessBaseAPI();

//printf(“tesseract-ocr version > %s\n”, ocr->Version());
//printf(“leptonica version > %s\n”, getLeptonicaVersion());

std::cout << "tesseract-ocr-" << ocr->Version() << std::endl;
std::cout << getLeptonicaVersion() << std::endl;

if (ocr->Init(NULL, lan, tesseract::OEM_DEFAULT)) {
 std::cout << "tesseract-ocr initialize error" << std::endl;
 return -1;
}


FILE* in = fopen(img_path, "rb");
if (in == NULL) {
 std::cout << "can not open > " << img_path << std::endl;
 return -1;
}
fclose(in);


//STRING text;
//if (! ocr->ProcessPages(img_path, NULL, 0, &text)) {
// std::cout << "page processing error" << std::endl;
// return -1;
//} else
// std::cout << text.string() << std::endl;


Pix *img = pixRead("extrabigresized.png");
ocr->SetImage(img);

char *text;
text = ocr->GetUTF8Text();
std::cout << text << std::endl;

delete [] text;
pixDestroy(&img);


ocr->End();


return 0;


}