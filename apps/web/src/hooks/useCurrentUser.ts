import { useQuery } from "@tanstack/react-query";

import { AuthService } from "@/services/auth.service";
import { useAuthStore } from "@/store/auth.store";

export function useCurrentUser() {
  const accessToken = useAuthStore(
    (state) => state.accessToken,
  );

  const user = useAuthStore(
    (state) => state.user,
  );

  const setUser = useAuthStore(
    (state) => state.setUser,
  );

  const query = useQuery({
    queryKey: ["auth", "me"],
    queryFn: AuthService.me,
    enabled: Boolean(accessToken) && user === null,
    retry: false,
  });

  if (query.data && user === null) {
    setUser(query.data);
  }

  return {
    ...query,
    user: query.data ?? user,
  };
}