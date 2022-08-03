import pandas as pd
from dataclasses import dataclass


def main():
    data = Data()
    print(data.get_result_dataframe())


@dataclass
class Data:
    customer_data_file_path = '~/Documents/FanDual_Technical_Interview_Materials/csv_files/customer.csv'
    sportsbook_bets_file_path = '~/Documents/FanDual_Technical_Interview_Materials/csv_files/sportsbook_bets.csv'

    def get_result_dataframe(self):
        joined_df = self.get_joined_dataframe()
        joined_df = joined_df.dropna()
        joined_df['concat_column'] = joined_df['customer_id'].astype(str) + ' ' + joined_df['bet_state']

        list_obj = joined_df['concat_column'].unique().tolist()

        result_df = pd.DataFrame(list_obj)
        result_df = result_df[0].str.split(' ', expand=True)
        result_df.rename(columns={0: 'customer_id', 1: 'bet_state'}, inplace=True)
        result_df = result_df.groupby('customer_id')['bet_state'].apply(list).reset_index()
        result_df['customer_id'] = result_df.index

        return result_df

    def get_joined_dataframe(self):
        joined_dataframe = self.get_customer_data().merge(self.get_sportsbook_bets_data(), on='customer_id', how='left')
        return joined_dataframe[['customer_id', 'bet_state']]

    def get_customer_data(self):
        customer_dataframe = pd.read_csv(self.customer_data_file_path)
        return customer_dataframe

    def get_sportsbook_bets_data(self):
        sports_book_bets_dataframe = pd.read_csv(self.sportsbook_bets_file_path)
        return sports_book_bets_dataframe


if __name__ == '__main__':
    main()
