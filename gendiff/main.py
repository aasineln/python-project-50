from gendiff.scripts.args_parser import get_args
from gendiff.scripts.gendiff import generate_diff


def main() -> None:
    args = get_args()
    result = generate_diff(
        file_path1=args.first_file,
        file_path2=args.second_file,
        format_type=args.format,
    )
    print(result)


if __name__ == "__main__":
    main()
