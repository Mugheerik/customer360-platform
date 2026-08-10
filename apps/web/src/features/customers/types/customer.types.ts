export type CustomerStatus = "active" | "inactive";

export type Customer = {
  id: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string | null;
  status: CustomerStatus;
  created_at: string;
  updated_at: string;
};

export type CustomerCreate = {
  first_name: string;
  last_name: string;
  email: string;
  phone?: string | null;
};

export type CustomerUpdate = {
  first_name?: string;
  last_name?: string;
  email?: string;
  phone?: string | null;
  status?: CustomerStatus;
};

export type CustomerSortField =
  | "created_at"
  | "first_name"
  | "last_name"
  | "email";

export type SortOrder = "asc" | "desc";

export type CustomerListParams = {
  search?: string;
  status?: CustomerStatus;
  page?: number;
  size?: number;
  sort?: CustomerSortField;
  order?: SortOrder;
};

export type CustomerListResponse = {
  items: Customer[];
  total: number;
  page: number;
  size: number;
  pages: number;
};

export type CustomerTimelineItem = {
  id: string;
  entity_type: string;
  entity_id: string;
  action: string;
  performed_by: string | null;
  details: Record<string, unknown> | null;
  created_at: string;
};