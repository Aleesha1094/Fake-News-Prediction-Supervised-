import csv


class NewsCSVWriter:
    def __init__(self, label, news):
        self.label = label
        self.news = news

    def write_to_csv(self):
        data = {'Label': [self.label], 'News': [self.news]}

        with open('fake_news_detector/Dataset.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Check if the file is empty
            is_empty = csvfile.tell() == 0

            if is_empty:
                writer.writerow(['Label', 'News'])

            writer.writerow([self.label, self.news])

        print('Data written to CSV successfully!')



