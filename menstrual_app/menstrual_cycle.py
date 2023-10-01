from datetime import datetime, timedelta


class MenstrualCalculator:

    @staticmethod
    def add_days_to_date(date_inputted, days):
        try:
            date_format = "%Y-%m-%d"
            end_date = datetime.strptime(date_inputted, date_format)
            result_date = end_date + timedelta(days=days)
            return result_date.strftime(date_format)
        except ValueError as e:
            raise ValueError(
                "Date format is Invalid. Correct Format ('yyyy-mm-dd')"
            ) from e

    def get_ovulation_day(self, date_last_period_started, cycle_length, flow_days):
        days_to_ovulation = (cycle_length + flow_days) // 2
        return self.add_days_to_date(date_last_period_started, days_to_ovulation)

    def get_start_of_fertility_date(self, ovulation_date):
        return self.add_days_to_date(ovulation_date, -2)

    def get_end_of_fertility_date(self, ovulation_date):
        return self.add_days_to_date(ovulation_date, 2)

    def get_start_date_of_next_period(self, date_last_period_started, cycle_length, flow_days):
        full_cycle = cycle_length + flow_days
        return self.add_days_to_date(date_last_period_started, full_cycle)

    def get_end_date_of_next_period(self, start_date_of_next_period, flow_days):
        return self.add_days_to_date(start_date_of_next_period, flow_days)

    def get_start_of_safe_period(self, date_last_period_started, number_of_flow_days):
        return self.add_days_to_date(date_last_period_started, number_of_flow_days + 1)

    def get_end_of_safe_period(self, date_last_period_start, cycle_length, flow_days):
        ovulation_date = self.get_ovulation_day(date_last_period_start, cycle_length, flow_days)
        return self.add_days_to_date(ovulation_date, -3)
