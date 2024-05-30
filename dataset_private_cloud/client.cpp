#include <iostream>
#include <fstream>
#include <boost/asio.hpp>
#include <chrono>
#include <string>

using boost::asio::ip::tcp;
using namespace std::chrono;

const int CHUNK_SIZE = 1024;

const std::string FILE_PATH = "./../../data/dataset.csv";
const std::string SERVER_HOST = "193.201.15.79";
const std::string SERVER_PORT = "7709";

void receive_file(tcp::socket& socket, const std::string& file_path) {
    std::ofstream file(file_path, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Could not open the file for writing!" << std::endl;
        return;
    }

    char buffer[CHUNK_SIZE];
    boost::system::error_code error;
    while (size_t len = socket.read_some(boost::asio::buffer(buffer), error)) {
        if (error == boost::asio::error::eof) break;
        if (error) throw boost::system::system_error(error);
        file.write(buffer, len);
    }

    file.close();
}

int main() {
    try {
        boost::asio::io_service io_service;
        tcp::resolver resolver(io_service);
        tcp::resolver::query query(SERVER_HOST, SERVER_PORT);
        tcp::resolver::iterator endpoint_iterator = resolver.resolve(query);

        tcp::socket socket(io_service);
        boost::asio::connect(socket, endpoint_iterator);

        std::cout << "---------------------------------------------" << std::endl;
        std::cout << "Connected to server" << std::endl;

        auto start = high_resolution_clock::now();

        receive_file(socket, FILE_PATH);

        auto end = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end - start).count();

        std::cout << "Dataset received" << std::endl;
        std::cout << "Time taken to receive dataset: " << duration << " milliseconds" << std::endl;
        std::cout << "---------------------------------------------" << std::endl;

    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}
