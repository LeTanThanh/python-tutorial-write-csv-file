if __name__ == "__main__":
  import csv

  # header = ["name", "area", "country_code2", "country_code3"]
  # data = [
  #   ["Albania", 28748, "AL", "ALB"],
  #   ["Algeria", 2381741, "DZ", "DZA"],
  #   ["American Samoa", 199, "AS", "ASM"],
  #   ["Andorra", 468, "AD", "AND"],
  #   ["Angola", 1246700, "AO", "AGO"]
  # ]

  # with(open("countries.csv", "w", encoding = "utf8")) as file:
  #   writer = csv.writer(file)
  #   writer.writerow(header)
  #   writer.writerows(data)

  fieldnames = ["name", "area", "country_code2", "country_code3"]
  rows = [
    {
      "name": "Albania",
      "area": 28748,
      "country_code2": "AL",
      "country_code3": "ALB"
    },
    {
      "name": "Algeria",
      "area": 2381741,
      "country_code2": "DZ",
      "country_code3": "DZA"
    },
    {
      "name": "American Samoa",
      "area": 199,
      "country_code2": "AS",
      "country_code3": "ASM"
    }
  ]

  with(open("countries.csv", "w", encoding = "utf8")) as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(rows)
