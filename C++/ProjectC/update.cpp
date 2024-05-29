#include "update.h"

Json::Value urls, names;
Json::Reader reader;
std::vector<std::string> urls_array, names_array;
bool urls_parse, names_parse;
std::string urls_string = "urls.json";
std::string names_string = "name.json";

/*
data_buffer is a pointer that will recive the data from the request
size_t size will be the amount of the size in bytes from data_buffer
size_t num_of_elem is the number of elements from the data_buffer
*/
static size_t size_of_data(char* data_buffer, size_t size, size_t num_of_elem, void* user_data) {
    size_t total_size = size * num_of_elem; // total_size will get the amount of data
    std::string *response_str = (std::string *)user_data; // response from HTTP request
    response_str->append(data_buffer, total_size); // response_str will recieve a value that contain JSON data or HTML, depends
    return total_size; // return the amount of data from the request in bytes
}

void get_data(std::string currency_url, std::string rate_file) {
    CURL *curl = curl_easy_init(); // new CURL handle

    if (curl) { // Checking if curl is not null
        std::string response; // response code from the request
        curl_easy_setopt(curl, CURLOPT_URL, currency_url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, size_of_data);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        
        if (res == CURLE_OK) {
            Json::Value new_file;
            Json::Reader file_reader;
            bool success = file_reader.parse(response, new_file);
            if (!success) {
                throw std::runtime_error("Failed to parse JSON file");
            } else {
                // Update the data from the web
                std::ofstream create_new_file("data/" + rate_file);
                create_new_file << new_file;
                create_new_file.close();
            }
        } else {
            throw std::runtime_error("Request Failed");
        }
    } else {
        std::cout << "49" << std::endl;
        std::exit(EXIT_FAILURE);
    }
}

void read_data() {
    // Reading the files
    std::fstream urls_read(urls_string);
    std::fstream names_read(names_string);
    urls_parse = reader.parse(urls_read, urls);
    names_parse = reader.parse(names_read, names);
    // Trying to read the files 
    if (!urls_read.is_open() || !names_read.is_open()) {
        throw std::runtime_error("Failed to open JSON file");
    }

    if (!urls_parse || !names_parse) {
        throw std::runtime_error("Failed to parse JSON file");
    }

    urls_read.close();
    names_read.close();
}

void convert_to_list() {
    read_data();
    Json::Value::Members names_keys = names.getMemberNames();
    Json::Value::Members urls_keys = urls.getMemberNames();
    size_t num_of_keys = names_keys.size();

    for (size_t i = 0; i < num_of_keys; i++) {
        names_array.push_back(names[names_keys[i]].asString());
        urls_array.push_back(urls[urls_keys[i]].asString());
    }

    // Sorting the array by the A B C, std::sort does that by ASCII code 
    std::sort(names_array.begin(), names_array.end());
    std::sort(urls_array.begin(), urls_array.end());
}

void create_data() {
    convert_to_list();
    // Creating the updated Data
    for (size_t i = 0; i < urls_array.size(); i++) {
        get_data(urls_array[i], names_array[i]);
    }
}

void update_data() {
    std::filesystem::path data_dir("data");; // Point to the data folder that contains values to perform request
    std::filesystem::path urls_file = data_dir / urls_string; // urls.json
    std::filesystem::path names_file = data_dir / names_string; // name.json

    if(!std::filesystem::exists(data_dir)) { // Checks if the directory is existing, this condition will execute only if the directory is not created
        std::filesystem::create_directories(data_dir); // Creating directory

        if (!std::filesystem::exists(urls_file) && !std::filesystem::exists(names_file)) {
            Json::Value new_urls_file, new_names_file;
            std::ofstream urls_new_file("data/" + urls_string);
            std::ofstream names_new_file("data/" + names_string);

            for (const auto& country_urls : country_urls) {
                std::istringstream iss(country_urls);
                std::string country, country_url;
                std::getline(iss, country, ':');
                std::getline(iss, country_url);
                new_urls_file[country] = country_url;
            }

            for (const auto& country_names : country_names) {
                std::istringstream iss(country_names);
                std::string country, country_name;
                std::getline(iss, country, ':');
                std::getline(iss, country_name);
                new_names_file[country] = country_name;
            }


            if (urls_new_file.is_open()) {
                urls_new_file << new_urls_file;
                urls_new_file.close();
            } else {
                std::cerr << "Unable to create urls.json file\n";
            }

            if (names_new_file.is_open()) {
                names_new_file << new_names_file;
                names_new_file.close();
            } else {
                std::cerr << "Unable to create name.json file\n";
            }
            
            // Creating the updated data
            create_data();
        } else {
            std::cout << "61" << std::endl;
        }
    } else {
        create_data();
    }
}