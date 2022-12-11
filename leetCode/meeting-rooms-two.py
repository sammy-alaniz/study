import heapq

class Solution:
#    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#        if len(intervals) == 0:
#            return 0
#
#        conference_rooms = [[intervals[0]]]
#        del intervals[0]
#
#        print(conference_rooms)
#
#        for unscheduled_meeting_time in intervals:
#            for room_meeting_list in conference_rooms:
#                for scheduled_meeting_time in room_meeting_list:
#
#                    # if scheudled meeting end time is less than unscheduled start meeting time, add to conf room
#                    if scheduled_meeting_time[1] < unscheduled_meeting_time[0]:
#                        room_meeting_list.append(unscheduled_meeting_time)
#
#        
#
#        
#
#        print(conference_rooms)
#
#        return 0

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

if __name__ == "__main__":
    sol = Solution()
    array = [[0,30],[5,10],[15,20]]
    num_rooms = sol.minMeetingRooms(array)
    print('number of rooms needed ' + str(num_rooms))