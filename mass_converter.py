def convert_mass(value, from_unit, to_unit):
    to_kg = {
        'г': 0.001,
        'кг': 1.0,
        'т': 1000.0,
        'фунт': 0.45359237,
        'lb': 0.45359237,
        'унция': 0.028349523125,
        'oz': 0.028349523125
    }

    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in to_kg:
        raise ValueError(f"Неизвестная исходная единица: {from_unit}")
    if to_unit not in to_kg:
        raise ValueError(f"Неизвестная целевая единица: {to_unit}")

    kg = value * to_kg[from_unit]
    result = kg / to_kg[to_unit]
    return result


def main():
    print("Конвертер массы")
    print("Поддерживаемые единицы: г, кг, т, фунт (или lb), унция (или oz)")

    try:
        value = float(input("Введите значение массы: "))
        if value < 0:
            print("Масса не может быть отрицательной.")
            return

        from_unit = input("Из какой единицы конвертировать? (например: кг): ")
        to_unit = input("В какую единицу конвертировать? (например: фунт): ")

        result = convert_mass(value, from_unit, to_unit)

        print(f"\n{value} {from_unit} = {result:.6g} {to_unit}")

    except ValueError as e:
        if "could not convert" in str(e):
            print("Ошибка: введите корректное число.")
        else:
            print("Ошибка:", e)
    except Exception as e:
        print("Произошла непредвиденная ошибка:", e)


if __name__ == "__main__":
    main()