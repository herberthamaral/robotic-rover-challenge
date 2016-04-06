from robot import robot

def test_rover_without_moves_should_do_nothing():
    position=(1,2,'N')
    final_position = robot(position=position, movements=[])
    assert position == final_position
