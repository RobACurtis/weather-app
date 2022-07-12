export default function getTime(time) {
  const milliseconds = time * 1000;
  const dateObj = new Date(milliseconds)
  const newTime = dateObj.toString();
  return newTime;
}
