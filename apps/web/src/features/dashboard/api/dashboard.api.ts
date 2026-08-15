import { api } from "@/lib/api/client";

import type { DashboardSummary } from "../types/dashboard.types";

export const DashboardService = {
  async getSummary(): Promise<DashboardSummary> {
    const response = await api.get<DashboardSummary>(
      "/dashboard/summary",
    );

    return response.data;
  },
};