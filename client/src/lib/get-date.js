export default function getDate(date) {
  const milliseconds = date * 1000;
  const dateObj = new Date(milliseconds)
  let newDate = dateObj.toDateString()
  const weekday = {
    'Mon':"Monday",
    'Tue':"Tuesday",
    'Wed':"Wednesday",
    'Thu':"Thursday",
    'Fri':"Friday",
    'Sat':"Saturday",
    'Sun':"Sunday"
  }

    const months = {
      'Jan': 'January',
      'Feb': 'Febuary',
      'Mar': 'March',
      'Apr': 'April',
      'May': 'May',
      'Jun': 'June',
      'Jul': 'July',
      'Aug': 'August',
      'Sep': 'September',
      'Oct': 'October',
      'Nov': 'November',
      'Dec': 'December',
    }

  const splitDate = newDate.split(" ");
  console.log(weekday[splitDate[0]]);

  newDate = weekday[splitDate[0]] + ' ' + months[splitDate[1]] + ' ' + splitDate[2] + ', ' + splitDate[3];
  return newDate;
}
