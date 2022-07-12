export default function getTime(time, timezone) {
  const milliseconds = time * 1000;
  const dateObj = new Date(milliseconds, )
  const newTime = dateObj.toLocaleTimeString('en-US', {timeZone: timezone})
  return newTime;
}
