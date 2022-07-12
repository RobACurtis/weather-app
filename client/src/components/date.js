export default function getDate(date) {
  const milliseconds = date * 1000;
  const dateObj = new Date(milliseconds)
  const newDate = dateObj.toDateString()
  return newDate;
}
