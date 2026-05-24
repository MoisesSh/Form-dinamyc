export const paramsConstructor = (object: Object) => {
  return Object.entries(object)
    .map((v) => {
      return `${v[0]}=${v[1]}`;
    })
    .toLocaleString()
    .replaceAll(",", "?");
};
