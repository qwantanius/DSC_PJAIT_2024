#include <iostream>
#include <fstream>
#include <boost/asio.hpp>
#include <string>

using boost::asio::ip::tcp;

const int CHUNK_SIZE = 1024;
const std::string READ_DATASET_FROM = "/home/int0x80/NYPD_Complaint_Data_Historic.csv";
const int RUN_PORT = 7709;

void send_file(tcp::socket& socket, const std::string& file_path) 
{
    std::ifstream file(file_path, std::ios::binary);
    if (!file.is_open()) 
    {
        std::cerr << "Could not open the file!" << std::endl;
        return;
    }

    char buffer[CHUNK_SIZE];
    
    while (file.read(buffer, CHUNK_SIZE) || file.gcount() > 0) 
    {
        boost::asio::write(socket, boost::asio::buffer(buffer, file.gcount()));
    }

    file.close();
}

int main()
{
    try {
        boost::asio::io_service io_service;
        tcp::acceptor acceptor(io_service, tcp::endpoint(tcp::v4(), RUN_PORT));

        while (true) 
        {
            tcp::socket socket(io_service);
            acceptor.accept(socket);
            std::cout << "Client connected" << std::endl;
            send_file(socket, READ_DATASET_FROM);
            std::cout << "File sent" << std::endl;
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}
