import useSWR from "swr";
export const useFetchTransform = ({
  key,
  fn,
}: {
  key: string;
  fn: () => void;
}) => {
  const { data, isLoading, error, isValidating, mutate } = useSWR(
    key,
    async () => fn(),
  );
  return { data, isLoading, error, isValidating, mutate };
};
