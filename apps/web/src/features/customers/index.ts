export { CustomerService } from "./api/customer.api";
export { NoteService } from "./api/note.api";
export { TaskService } from "./api/task.api";

export type {
  Customer,
  CustomerCreate,
  CustomerListParams,
  CustomerListResponse,
  CustomerStatus,
  CustomerTimelineItem,
  CustomerUpdate,
  CustomerSortField,
  SortOrder,
} from "./types/customer.types";

export type {
  Note,
  NoteCreate,
  NoteUpdate,
} from "./types/note.types";

export type {
  Task,
  TaskCreate,
  TaskPriority,
  TaskStatus,
  TaskUpdate,
} from "./types/task.types";