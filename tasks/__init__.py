
class TaskStatus:
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    BLOCKED = 'BLOCKED'
    REVIEW = 'REVIEW'
    COMPLETED = 'COMPLETED'

    CHOICES = (
        (TODO, 'TODO'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (BLOCKED, 'BLOCKED'),
        (REVIEW, 'REVIEW'),
        (COMPLETED, 'COMPLETED')
    )
