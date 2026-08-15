export type DashboardActivity = {
  id: string;
  entity_type: string;
  entity_id: string;
  action: string;
  actor_id: string | null;
  details: Record<string, unknown> | null;
  created_at: string;
};

export type DashboardSummary = {
  total_customers: number;
  active_customers: number;
  new_customers: number;
  organizations: number;
  recent_activity: DashboardActivity[];
};