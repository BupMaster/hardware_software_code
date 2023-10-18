def print_meters_to_cm(meters):
    print(100 * meters)

def return_meters_to_cm(meters):
    return 100 * meters

def main():
    print_cm = None
    return_cm = return_meters_to_cm(2)
    print(return_cm)

if __name__ == "__main__":
    main() 