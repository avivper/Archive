#ifndef UPDATE_H
#define UPDATE_H

#include <fstream>
#include <stdexcept>
#include <curl/curl.h>
#include <json/json.h>
#include <filesystem>
#include "calc.h"

extern std::vector<std::string> country_urls;
extern std::vector<std::string> country_names;

void update_data();

#endif